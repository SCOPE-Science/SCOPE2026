# Mathematical review

## Correctness — PASS

The component-kernel argument explicitly handles graph edges, zero supports, isolated vertices, disconnected graphs, all fields including characteristic two, and the quantifiers \(q\) prime power and \(t\ge1\). Counting projective directions and nonzero scalar representatives yields the stated product. At \(T=1\) it totals \(q^{t(n+m)}\); the sharp rank maxima and center-cutting claim follow directly. The independent implementation of row elimination checks 132 representative and exhaustive cases covering 400389 vertex tuples and includes the extension field \(\mathbb F_4\). Finite checks supplement the symbolic proof rather than certify all cases.

## Originality — PASS, with residual bibliographic uncertainty

The closest published exact comparison is Rossmann's 2022 class-size polynomial (Eq. (1.2)), which is **exactly the known \(t=1\) case**. The current claim excludes that as an original contribution: it addresses all \(t\ge2\), with projective support-component factors and simultaneous-orbit multiplicities, neither stated nor implied by the single-element formula without another common-kernel classification. Mainkar's 2015 paper establishes graph-faithfulness; DeCoste--DeMeyer--Mainkar's 2015 preprint treats a different central-indexed \(j(Z)\) operator. Targeted published-finding corpus searches found no equivalent tuple enumeration. Unindexed or differently named prior work remains a risk.

## Value — PASS

Common centralizer dimensions govern simultaneous conjugation of ordered tuples and are natural higher invariants of finite Lie algebras and graphical groups. The general graph-sum determines all stabilizer ranks, provides a closed orbit-size count, and sharply distinguishes single-element and pair behavior: one cannot cut to the center in a nonabelian graph Lie algebra, but two always suffice even over \(\mathbb F_2\). The binary four-vertex path and star have different joint rank distributions despite identical vertex and edge counts.

## Sources, limits, and checks

Original construction: Mainkar, *Graphs and two-step nilpotent Lie algebras* (arXiv:1310.3414v1; 2015 publication). Related metric operator: DeCoste--DeMeyer--Mainkar (arXiv:1512.07944v1). Closest exact t=1 polynomial and group-Lie centralizer equivalence: Rossmann (arXiv:2107.05564v1; DOI:10.1112/blms.12665). The support formula is exponential in graph size and does not distinguish all graph isomorphism types by assertion. Independent external mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
