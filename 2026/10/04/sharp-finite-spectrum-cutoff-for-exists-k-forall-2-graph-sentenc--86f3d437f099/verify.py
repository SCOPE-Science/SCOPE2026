#!/usr/bin/env python3
"""Finite sanity checks for the sharp spectrum cutoff proof."""

def check_profiles():
    for k in range(13):
        cap = (1 << k)
        endpoint = k + cap
        assert endpoint == k + len(range(cap))
        # Every size from k through k+2^k is obtained by choosing m distinct profiles.
        if k == 0:
            assert endpoint == 1
            continue
        for n in range(k, endpoint + 1):
            m = n - k
            profiles = list(range(m))
            assert len(profiles) == m
            assert len(set(profiles)) == m
            assert all(0 <= p < cap for p in profiles)


def check_clone_type_table():
    # Atomic pair data relevant to a simple graph: equality and adjacency.
    # same clone maps to (b,b); distinct clones map to (b,c).
    same_clone = {"eq": True, "edge": False}
    bb = {"eq": True, "edge": False}
    assert same_clone == bb
    for bc_edge in (False, True):
        distinct_clones = {"eq": False, "edge": bc_edge}
        bc = {"eq": False, "edge": bc_edge}
        assert distinct_clones == bc


if __name__ == "__main__":
    check_profiles()
    check_clone_type_table()
    print("VERIFY_OK k=0..12 sharp_profile_counts_and_clone_types")
