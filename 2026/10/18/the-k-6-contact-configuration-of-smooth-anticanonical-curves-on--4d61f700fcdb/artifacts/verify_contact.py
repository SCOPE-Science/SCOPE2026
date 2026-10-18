"""Exact intersection calculation for one representative pair of cubics.
The symmetry verifier proves transitivity on all 15 unordered pairs.
"""
import sympy as sp,json
X,Y,Z,s,t=sp.symbols('X Y Z s t')
F=X**2*Y+X**2*Z+X*Y**2+Y*Z**2
G=X**2*Z+X*Y**2+X*Z**2+Y*Z**2
P=sp.Poly(F+G,X,Y,Z,modulus=2)
assert P==sp.Poly(X*(X*Y+Z**2),X,Y,Z,modulus=2)
L=sp.Poly(F.subs({X:0,Y:1,Z:t}),t,modulus=2)
Q=sp.Poly(F.subs({X:s**2,Y:t**2,Z:s*t},simultaneous=True),s,t,modulus=2)
assert L==sp.Poly(t**2,t,modulus=2)
assert Q==sp.Poly(s**4*t*(t+s),s,t,modulus=2)
# At (0:1:0), the component X=0 contributes order 2, the
# component XY+Z^2 contributes order 4; others contribute order 1.
# The four base points are simple points of both cubics, so blowing
# up reduces their intersection multiplicity by one at each point.
result={'representative_cubic_masks':[7,22],
'pair_sum_factorization':'X*(X*Y+Z**2)',
'line_contact_order_at_010':2,
'conic_contact_order_at_010':4,
'plane_intersection_multiplicities_at_base_points':{'(0:1:0)':6,'(0:0:1)':1,'(1:0:0)':1,'(1:1:1)':1},
'plane_intersection_total':9,
'blown_up_intersection_multiplicity_at_unique_common_point':5,
'anticanonical_self_intersection':5,
'other_geometric_intersections':0}
print(json.dumps(result,indent=2,sort_keys=True))
