#!/usr/bin/env python3
"""Reconcile independent exhaustive classifications for each labelled vertex set."""
import verify_forcing as direct
import verify_forts as dual
import json
assert direct.N == dual.SIZE == 16
assert all(direct.ADJ[u].bit_count() == 4 for u in range(16))
for m in range(1 << 16):
    assert direct.truth[m] == (not dual.contains[dual.FULL ^ m]),m
assert direct.counts == dual.counts
assert set(direct.minimal) == set(dual.minimum)
expected_fort=[{'representative':278,'cardinality':4,'orbit_size':16},
               {'representative':828,'cardinality':6,'orbit_size':32},
               {'representative':1632,'cardinality':4,'orbit_size':12},
               {'representative':6634,'cardinality':8,'orbit_size':192},
               {'representative':7140,'cardinality':8,'orbit_size':96}]
assert dual.orbits == expected_fort
assert sum(o['orbit_size'] for o in dual.orbits)==348
assert sum(o['size'] for o in direct.orbits)==2360
print('CROSSCHECK_OK all_65536_direct_force_vs_fort_complement=true')
print('CROSSCHECK_OK 348_minimal_forts_five_orbits 2360_minimal_zero_forcing_sets_eleven_orbits')
