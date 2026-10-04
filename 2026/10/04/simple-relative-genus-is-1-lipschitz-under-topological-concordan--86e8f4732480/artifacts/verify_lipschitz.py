#!/usr/bin/env python3
"""Finite regression for the ceiling/zero-genus lemma in the Lipschitz proof."""
import math

def genus_from_score(score, disc_allowed, b2):
    if score <= b2 and disc_allowed:
        return 0
    return max(1, math.ceil((score - b2) / 2))

checked = 0
for b2 in range(0, 16):
    for s1 in range(0, 64):
        for s2 in range(0, 64):
            for h in range(0, 16):
                if abs(s1 - s2) > 2 * h:
                    continue
                for d1 in (False, True):
                    for d2 in (False, True):
                        if h == 0 and d1 != d2:
                            continue
                        g1 = genus_from_score(s1, d1, b2)
                        g2 = genus_from_score(s2, d2, b2)
                        assert abs(g1 - g2) <= h
                        checked += 1
print(f"VERIFY_OK cases={checked} b2=0..15 scores=0..63 h=0..15")
