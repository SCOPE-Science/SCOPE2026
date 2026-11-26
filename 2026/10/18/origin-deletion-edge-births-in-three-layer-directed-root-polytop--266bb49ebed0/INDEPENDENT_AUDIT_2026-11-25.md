# Independent mathematical audit

## correctness

PASS

All roots have norm √2 and are distinct, hence exposed. Constant score on all roots forces constant potentials within each part and then equality of the three part potentials, as the AB and BC differences add to the AC difference. This gives the full zero-sum affine dimension, including singleton parts. The same-block face is a product of simplices. The specified strict potentials for shared-tail AB/AC, shared-head AC/BC, and noncomposable AB/BC have positive maximum attained exactly twice; for the last one the AC shortcut has score zero, below the common score one. Each excluded disjoint-tail/head or composable pair with b≥2 has an alternative root-pair sum, so it cannot be a strict two-vertex maximum. For b=1 the composable pair is exposed by the displayed negative potential and any exposing potential must be negative because the shortcut's score is twice the common score. This proves the origin comparison, since the origin maximizes the increasing-layer potential, no negative witness survives its addition, and a positive witness survives. Within-block edge counts are pq(p+q−2)/2, mixed counts are abc, abc and ac[b(b−1)+1_(b=1)]; direct incidence counts give the degrees. A swapped coordinate or the shortcut is a common neighbor for each nonedge. A nonedge exists if a>1 (different AB/AC tails), c>1 (different AC/BC heads), or b>1 (composable pair), so exactly the singleton triple has diameter one. Comparing each degree to dimension gives the stated simplicity thresholds. Inspected verify.py's strict-score and alternative-sum tests; the reported 125 finite profiles corroborate the arguments but were not rerun.

## originality

PASS

The supported distinction is the complete non-origin-adjoined edge classification and the exact origin-deletion threshold for complete three-layer digraphs. Existing acyclic origin-adjoined face results already cover the surviving edges, and general facet machinery exists for P. Neither those statements nor the transitive-tournament census supply the threshold and the complete non-adjoined graph by direct specialization.

## value

PASS

Three layers are the first complete transitively layered case with both paths and shortcuts and no rank function. The exact graph gives usable degrees, simplicity, and a sharp deletion effect: a singleton middle part gives one new edge per outer pair, so the effect can be quadratic, while adding one middle vertex eliminates it. This is a naturally parameterized structural distinction, not a finite enumeration or a rewording of the full tournament result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
