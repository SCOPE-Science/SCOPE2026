# Independent audit — 2026-09-29

Record: `2026/09/13/002`  
Audited source tree: `a0bc73831fe833d394d886dc31e67720af975320`  
Disposition: **repaired**

## Correctness

The exact class-algebra numbers are correct. An independent S_9 conjugacy-class transition calculation gives H((6,2,1),(5,4);r=3)=324 and H((3,3,3),(5,4);r=3)=40. Peeling the last transposition produces exactly the five children (9), (4,4,1), (4,3,2), (5,3,1), (5,2,2), with coefficients 9,8,6,3,4 and factor differences -15,-6,-20/3,-37/3,-6, giving terms -135,-48,-40,-37,-24 and total -284. The segment between the two profiles does cross two resonance walls. The scientific defect is attribution: the displayed five-term equation is the ordinary class-algebra cut/join (last-transposition) decomposition, not the Shadrin-Shapiro-Vainshtein neighboring-chamber wall-crossing formula. SSV explicitly treats differences of chamber polynomials across a single wall. The staged repair preserves all exact enumeration and cut/join identities but removes the claim that this equation itself verifies the SSV wall-crossing identity.

## Originality

Piecewise polynomiality and genus-zero wall crossing are established by Shadrin-Shapiro-Vainshtein and later tropical work. The record's value is as a reproducible exact degree-9 class-algebra example, not as a new wall-crossing theorem.

## Scientific value

The two endpoint Hurwitz numbers and five-term cut/join decomposition form a useful exact consistency test across a multi-wall path once the stronger SSV-verification label is removed.

## Limitations

- The repaired five-term formula is a cut/join class-algebra identity, not a decomposition into the two individual resonance-wall crossings.
- No direct raw S_9 tuple enumeration was performed; the exact class-algebra calculation is independently reproducible.
- The repair does not claim a new SSV wall-crossing theorem or verification beyond consistency with the chamber framework.

## Evidence and literature

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/002
- https://arxiv.org/abs/math/0611442
- https://arxiv.org/abs/1003.1805
- https://doi.org/10.1016/j.aim.2007.06.016
- https://doi.org/10.1016/j.aim.2011.06.021
