# Independent mathematical audit

## correctness

PASS

The relations imply AP_B=P_BA and BP_A=P_AB, so the coordinate support strata are invariant. Outside the overlap there are two signed singleton choices per active generator and two label-preserving sign assignments per active transposition. On the overlap the two unsigned involutions commute. A one-point orbit cannot anticommute in characteristic other than two; if both involutions swap a two-point orbit, (AB)^2 would be both I and -I. With precisely one swap there are two choices of the swapping generator and four signed assignments per choice. On a four-point orbit the unsigned action is regular, with 4!/4 possible labeled actions, and exactly one independent parity equation on its four edge signs leaves eight assignments. These give the connected weights 8/2! and 48/4!, yielding exactly the stated joint EGF and its unrefined specialization, including n=0. The four-point signs are one conjugacy class: diagonal sign changes act with only the global sign in the kernel, transitively on the eight valid assignments, and coordinate permutations identify the regular unsigned actions. On a common two-point orbit a coordinate swap interchanges the opposite diagonal signs and a diagonal sign change can reverse the swap sign. Together with the one-active components this proves the stated component type counts and full-support parity. The source verifier tests only unrefined totals. An independently written exhaustive signed-product census for n=0 through 5 compared every joint support coefficient and found 1,5,37,305,2905,30125; at n=5 it checked 963 squared candidate pairs. A separate finite conjugacy census found two common two-point classes of size 4 and one common four-point class of size 48. Replay: python3 replay/2/independent_check.py and python3 replay/2/component_orbits.py. These are diagnostics, not the all-n argument.

## originality

PASS

The inspected comparisons support the distinct labeled signed-partial joint-rank enumerator, not novelty for the exponential formula, the parity obstruction for arbitrary invertible involutions, or general anticommutation theory. No equivalent or stronger enumeration was established by the bounded search.

## value

PASS

Literal anticommutation is a natural relation for involutions in the signed rook monoid, and the two support ranks are intrinsic invariants, not an arbitrary finite slice. The exhaustive structural decomposition explains precisely what the sign obstruction permits, and the resulting EGF gives the joint rank census in every dimension, including unequal domains. The scientific value is this exact classification and refined count, not the standard assembly step or the small verification table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
