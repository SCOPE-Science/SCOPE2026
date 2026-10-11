# Independent mathematical audit

## correctness

PASS

Ichihara's source reduces purely cosmetic surgery in the low-span regime to five derivative constraints at one and three root-of-unity constraints, and explicitly leaves span 12 because those equations alone admit nontrivial formal solutions. The frozen exact elimination solves the thirteen linear equations for each exponent residue \(R\bmod60\); the coefficient-matrix determinant is the nonzero constant 6,998,400,000, so the solution is unique. The extra knot condition \(|V(-1)|=1\), justified by trivial Alexander polynomial for a cosmetic-surgery knot, turns each residue family into two integer quartic equations. A fresh BigInt replay of the complete 60-residue certificate used the integer rational-root theorem and independently found exactly thirteen integer solutions: \((R,n)=(0,0)\) and \((48,-1),\ldots,(59,-1)\); reconstructing every Laurent polynomial gives the single monomial \(1\). Hence no nontrivial span-at-most-12 Jones polynomial survives.

## originality

PASS

Ichihara's paper proves the obstruction only through span 11, then devotes Section 6 to showing nontrivial formal span-12 solutions and explicitly says the determinant condition \(|f(-1)|=1\) is a further condition needed to extend the method and leaves that extension to future work. The submitted exhaustive symbolic elimination is exactly that first unresolved boundary. No later or independent source located already performs the sixty-family determinant closure.

## value

PASS

The result closes the first boundary explicitly left open by the current low-span Jones obstruction. It converts a source-identified necessary condition into a complete exact classification over all residue families and extends a knot-surgery obstruction by one full span level.

The dated certificate retains the supplied scientific assessment, sources and limitations.
