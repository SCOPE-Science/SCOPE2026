# Independent audit — 2026-09-29

Record: `2026/09/18/maximum-spectral-radius-strongly-connected-tricyclic-digraphs--e58d4b5b4bf1`  
Assigned and audited source tree: `eef50649b893da6c5a51138c82090ebc1c2f2339`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The first-return proof is correct. The excess-outdegree identity forces either one outdegree-3 vertex or two outdegree-2 vertices. In the one-branch case, the three deterministic first-return lengths satisfy sum ell_i>=m+2 and the Perron equation sum z^ell_i=1. The exponent-transfer inequality gives the unique maximizing multisets {1,2,m-1} with loops and {2,2,m-2} without loops. In the two-branch case, the 2x2 first-return matrix is irreducible and has spectral radius one at z=rho(G)^-1; each of the three endpoint patterns is strictly below the candidate value at r_m or s_m by the displayed determinant/row-sum inequalities. Independent exhaustive enumeration for m=3,4,5 agrees with the theorem: the loop-allowed maxima are respectively 2, 1.8392867552141619, and 1.7548776662466916, while the loopless maxima are the golden ratio for m=3, sqrt(3) for m=4, and the golden ratio for m=5, with the predicted rose isomorphism classes.

## Originality

**qualified_current_conjecture_resolution**. Klech's September 2026 preprint treats the minimum spectral-radius problem, classifies the m+2-arc class, and states the corresponding maximum problem as Conjecture 5.15. Current searches through 2026-09-29 did not locate a later proof of the two maximum formulas. Earlier bicyclic and subclass extremal results do not cover the whole tricyclic class. The audit therefore supports this as a resolution of a very recent conjecture, with the usual substantial concurrency risk created by the short priority window.

## Scientific value

**meaningful_sharp_extremal_theorem**. The theorem completes the maximum side of the newly classified excess-two problem with sharp values and unique extremizers, using a substantially shorter branching/first-return argument than a case-by-case eighteen-family comparison. The exact loopless analogue and uniqueness make the result more than a numerical confirmation of the conjecture.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/maximum-spectral-radius-strongly-connected-tricyclic-digraphs--e58d4b5b4bf1
- https://arxiv.org/abs/2609.18367
- https://doi.org/10.1016/j.laa.2011.09.018
- https://doi.org/10.1080/03081087.2021.1996523

## Limitations

- The theorem is specific to arc excess two and does not establish a general fixed-excess extremal theory.
- It uses the structural context of Klech's very recent preprint, although the first-return proof itself is self-contained once the degree pattern is observed.
- The conjecture is only weeks old, so not-yet-indexed parallel work cannot be excluded.
