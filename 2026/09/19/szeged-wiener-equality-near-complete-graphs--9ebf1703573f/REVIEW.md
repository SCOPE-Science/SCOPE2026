# Review

## Correctness

**PASS.** Let \(Q\cong K_q\) be the distinguished clique and let \(A=N_Q(x)\), \(B=N_Q(y)\) for the two remaining vertices. The four Venn-cell sizes \(a,b,c,d\) determine all distances and all Szeged edge contributions. Clique edges contribute \(\binom q2+(a+b)(c+d)+3ab+2cd\). The remaining edge contributions split according to whether \(xy\) is present and, when it is absent, whether \(A\cap B\) is empty. Subtracting the corresponding Wiener index gives the three displayed exact formulas in RESULT.md.

The 2-connectivity criterion is also exact: with \(xy\) present one needs nonempty \(A,B\) and at least two vertices in \(A\cup B\); without \(xy\), both \(A\) and \(B\) must have size at least two. Substituting these constraints into the exact formulas reduces \(\eta(G)=2n\) to elementary nonnegative integer equations. For \(xy\notin E\) there is no solution with \(q=n-2\ge8\). For \(xy\in E\) and \(c=0\), equality forces \(a=b=1\), giving the Zhang–Li family. For \(c>0\), the unique solution with \(q\ge8\) is \((a,b,c,d)=(0,1,1,6)\) or its transpose, giving the single additional order-10 isomorphism type.

The standalone verifier recomputes distances, Wiener indices, and Szeged indices from the definitions. It checks every connected Venn-cell parameter type with \(2\le q\le10\), and checks the equality classification through \(q=40\). All saved checks pass. The finite computation supports but is not used in the general proof.

## Originality

**PASS, to the best of our knowledge.** The accessible current full text of Zhang–Li, arXiv:2609.20025v1, was inspected. It proves the strengthened lower bound, explicitly poses classification of \(\eta(G)=2n\) as Problem 7, and gives the family \(G_n\) formed from \(K_{n-2}\) plus two adjacent degree-two vertices attached to distinct clique vertices. It does not give a clique-number slice of the equality classification or a general formula for two-vertex extensions of a clique.

The accessible primary preprint underlying Bonamy–Knor–Lužar–Pinlou–Škrekovski (2017), arXiv:1602.05184, was also inspected. It proves and classifies equality in the older \(2n-6\) bound and proposes the stronger \(2n\) conjecture, but does not contain the result here.

Targeted searches covered Szeged–Wiener gap/equality together with clique number, \((n-2)\)-cliques, near-complete graphs, two-vertex clique extensions, and the exact equation \(\eta(G)=2n\). No equivalent classification or the three-case formula was located. No specific inaccessible paper was identified as a plausible source that would overturn the originality claim. Residual risk remains from unindexed parallel work or older work using substantially different terminology.

## Value

**PASS.** The newest source leaves the equality case as an explicit open problem. This result solves that problem completely for the natural high-clique regime \(\omega(G)\ge n-2\): for every \(n\ge11\), the source paper's construction is uniquely forced, while \(n=10\) has one additional isomorphism type. The exact formulas for all two-vertex extensions of a clique are reusable beyond the equality application and expose how the four neighborhood-intersection cells control the Szeged–Wiener gap.

## Limitations

- The equality classification is restricted to graphs containing an \((n-2)\)-clique; equality graphs with smaller clique number are not classified.
- The newest source explicitly notes that its construction is not necessary in general, so further equality types are expected outside this regime.
- Finite exhaustive verification supports but does not replace the symbolic proof.
- Unindexed recent work or substantially different terminology remains a residual originality risk.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
