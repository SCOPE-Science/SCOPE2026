# Independent mathematical audit — SCOPE-20260912-073

Disposition: **passed**.

## Correctness
**PASS** — The character calculation is internally consistent and the decisive general-n decomposition can be reconstructed without trusting finite logs. In bidegree (2,0), the diagonal classes Delta_ij are independent. In bidegree (1,1), contributions split by triples and the local map has rank 4, producing the stated local cokernel character. For E₃ bidegree (0,2), projection to a target edge kills domain terms on disjoint edge pairs; the remaining sharing-edge terms split over triples, where the exact n=3 map is injective. Hence E₃ bidegree (0,2)=0 for all n. No higher differential can affect total degree 2, yielding P2=(1/3)X1 cubed+2X1X2+2X3+(3/2)X1 squared-X2-(11/6)X1 for every n. Its identity value equals 2 C(n,3)+5 C(n,2).

## Originality
**PASS** — Wawrykow studies secondary representation stability for the ordered once-punctured torus and derives Betti-growth information; Cheong-Huang compute unordered Betti/Hodge numbers for the punctured elliptic curve. Neither inspected source states this exact ordered S_n character polynomial or its all-n onset. Resultary returned this record as the only direct semantic match.

### Equivalent formulations
The claim is an exact S_n class function, strictly finer than the identity-character Betti number or unordered invariants.

### Broader coverage
Eventual stability does not mechanically imply the all-n formula.

### Exact database or table search
Database search supports but does not prove originality.

### Claim versus prior implication
Those statements do not imply character values on nonidentity conjugacy classes.

## Value
**PASS** — An exact low-degree S_n character and sharp onset are natural representation-stability data for a basic punctured surface. The result refines known Betti growth and can serve as a base case for FI-module and secondary-stability calculations.

## Source inspections
- **Wawrykow, Secondary representation stability and the ordered configuration space of the once-punctured torus** (arXiv:2008.11766): full arXiv HTML/abstract and paper structure Assessment: Studies ordered once-punctured-torus representation stability and generator growth, but does not state the exact H2 character polynomial in the inspected material. Evidence: The abstract emphasizes secondary stability and generation on at most four points, with Betti growth derived from prior work.
- **Cheong-Huang, Betti and Hodge numbers of configuration spaces of a punctured elliptic curve from its zeta functions** (arXiv:2009.07976 / Trans. AMS 375 (2022)): author-page abstract and publication summary Assessment: The stated object is the unordered configuration space; Betti/Hodge series do not determine the ordered S_n character. Evidence: The abstract explicitly describes unordered configuration spaces and their Betti/Hodge generating functions.
- **Resultary semantic search** (Resultary local research index): top hits for punctured-torus H2 character polynomial Assessment: SCOPE073 was the only direct exact match. Evidence: No stronger prior SCOPE statement with the same polynomial/onset was returned.

## Residual risks
- The all-n E₃ bidegree (0,2) vanishing rests on the stated edge-projection/triple-decomposition argument plus the exact n=3 local map; a fully formalized chain-level proof was not produced.
- No exact phrase match was treated as novelty proof.
