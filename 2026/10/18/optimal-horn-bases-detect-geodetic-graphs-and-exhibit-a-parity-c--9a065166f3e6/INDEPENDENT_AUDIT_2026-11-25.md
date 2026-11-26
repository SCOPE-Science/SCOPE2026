# Independent mathematical audit

## correctness

PASS

Original correctness FAIL: the frozen universal equivalence is false. The step from validity to membership of the head in I(u,v) is wrong for general graphs; validity only requires the iterated hull. In H5=K_{5,5} minus a matching, each same-shore pair forces three common neighbors; every vertex of the first shore then has two neighbors among those three, and the full first shore forces the second. A matched cross-shore pair already has the whole graph in its interval. Thus every nonedge has full hull, even though the graph has multiple shortest paths. The basis in the repair uses one unit rule per nonedge, iterating matched pair i to matched pair i+1 by two rules and making every same-shore pair enter this cycle. Its weight is 75=3M, refuting the necessity assertion. The delivered corrected finding drops that necessity, preserves geodetic sufficiency and the complete cycle census, and includes the crown only as a counterexample. In a geodetic graph every subpath is uniquely geodesic, so the hull of a pair really is its path; an arbitrary singleton split suffices by induction. The frozen even-cycle lower bound also failed to consider adding the second semicircle from a larger premise containing the antipodes. The repaired proof groups every potential escape rule by the unique antipodal pair in its semicircle. A premise missing either endpoint lies in a proper convex subarc, so cannot escape. Each group contains the compulsory pair rule and costs at least four; at four there can only be the single two-head pair rule, one head in each open side. No nonantipodal mandatory rule belongs to a group. Shorter-arc induction proves attainability and independence of choices. This gives the cost and factorial counts including C3 and C4. Replay `cd /workspace/repairs/3 && python3 verify.py`: considers all sound rules for C3–C5 by exact weighted set cover, tests all candidate optimum bases for C3–C7 and samples C8–C10, compares all subset models in H5–H7, and checks the H4 square obstruction. Finite experiments corroborate, not prove, the repaired all-size statements. The frozen source and its claims remain unchanged.

## originality

PASS

For the repaired result only: the full minimum literal-cost classification and all-bases counts on geodetic graphs and both cycle parities were not established by the inspected results. Crown tightness is covered as a consequence of full nonedge hulls and the Hamiltonian hydra theorem; it is credited and retained solely as a counterexample, not assessed as new. The false original converse is not passed.

## value

PASS

The corrected theorem answers the natural minimum-literal encoding problem over unrestricted bases and counts every optimum for two infinite cycle families. The even-cycle extra cost is a provable local obstruction that must be charged even in the presence of larger antecedents; the repaired census survives the failure of the global converse. The geodetic construction and explicit counterexample clarify what shortest-path uniqueness does and does not determine. The surviving value is not a claim of novelty for the known full-hull crown mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
