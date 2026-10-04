#!/usr/bin/env python3
"""Regression check for the half-turn symmetry in the published pure-braid constructor.

This reproduces only the coordinate formulas needed for the braid-carrying edges.
The theorem is proved symbolically in RESULT.md; this finite check is not the proof.
"""
import itertools
import math

LANE_SPACING = 0.90
CROSSING_Z = 0.32
SAMPLES = 7

def expand_word(word):
    out = []
    for ch in word:
        if ch == "A":
            out.extend((1, 1))
        elif ch == "B":
            out.extend((2, 2))
        else:
            raise ValueError(ch)
    return out

def body_paths(word):
    braid = expand_word(word)
    lanes = (LANE_SPACING, 0.0, -LANE_SPACING)
    if not braid:
        return [
            [(0.0, lanes[i], 0.0), (1.0, lanes[i], 0.0)]
            for i in range(3)
        ], 1.0

    points = {i: [(0.0, lanes[i], 0.0)] for i in range(3)}
    occupant = [0, 1, 2]

    for step, generator in enumerate(braid):
        pair = generator - 1
        upper_lane, lower_lane = pair, pair + 1
        upper_edge = occupant[upper_lane]
        lower_edge = occupant[lower_lane]
        lane_of = {occupant[lane]: lane for lane in range(3)}

        for edge_id in range(3):
            lane0 = lane_of[edge_id]
            if edge_id == upper_edge:
                lane1 = lower_lane
            elif edge_id == lower_edge:
                lane1 = upper_lane
            else:
                lane1 = lane0

            segment = []
            for j in range(SAMPLES):
                t = j / (SAMPLES - 1)
                smooth = 0.5 - 0.5 * math.cos(math.pi * t)
                bump = math.sin(math.pi * t)
                x = step + t
                y = (1.0 - smooth) * lanes[lane0] + smooth * lanes[lane1]
                if edge_id == upper_edge:
                    z = CROSSING_Z * bump
                elif edge_id == lower_edge:
                    z = -CROSSING_Z * bump
                else:
                    z = 0.0
                segment.append((x, y, z))
            points[edge_id].extend(segment[1:])

        occupant[upper_lane], occupant[lower_lane] = (
            occupant[lower_lane], occupant[upper_lane]
        )

    assert occupant == [0, 1, 2]
    return [points[i] for i in range(3)], float(len(braid))

def rotate(point, x_right):
    x, y, z = point
    return (x_right - x, y, -z)

def close(a, b, tol=2e-12):
    return max(abs(x-y) for x, y in zip(a, b)) <= tol

checked = 0
max_error = 0.0

for length in range(0, 11):
    for letters in itertools.product("AB", repeat=length):
        word = "".join(letters)
        left, x_right = body_paths(word)
        right, x_right_2 = body_paths(word[::-1])
        assert x_right == x_right_2

        for p, q in zip(left, right):
            transformed = [rotate(x, x_right) for x in reversed(p)]
            assert len(transformed) == len(q)
            for a, b in zip(transformed, q):
                err = max(abs(x-y) for x, y in zip(a, b))
                max_error = max(max_error, err)
                assert close(a, b), (word, a, b, err)
        checked += 1

print(
    "VERIFY_OK "
    f"words={checked} max_length=10 "
    f"max_coordinate_error={max_error:.3e}"
)
