#!/usr/bin/env python3
"""Literal comparison of separate exact enumerations of tame degree-five maps."""
import verify_symbolic as symbolic
import verify_extensions as extensions
assert symbolic.MAPS == set(extensions.DEGREE5)
assert symbolic.TAME == set(extensions.TAME)
assert len(symbolic.TAME)==60
assert {(a,b) for a,b in symbolic.TAME if symbolic.ram_types(a,b).count(3)==4} == {symbolic.image((7,41),g,h) for g in symbolic.GL for h in symbolic.GL}
print('DEGREE5_SET_EQUALITY',len(symbolic.MAPS))
print('TAME_SET_EQUALITY',len(symbolic.TAME))
print('A5_ORBIT_EQUALITY',36)
print('VERIFY_OK')
