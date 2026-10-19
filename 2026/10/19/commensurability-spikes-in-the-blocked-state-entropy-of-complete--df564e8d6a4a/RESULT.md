# Commensurability spikes in the blocked-state entropy of complete-bipartite Potts antiferromagnets

## Finding
Fix an integer \(q\ge3\). For all integers \(a,b\ge1\), a \(q\)-colour antiferromagnetic Potts configuration on the complete bipartite graph \(K_{a,b}\) is **one-site blocked** when no change of the colour at a single vertex *strictly lowers* the energy; **two-site blocked** means this for simultaneous changes at any one or two vertices. Energy-neutral changes are not accepted in either definition.

Let \(A_i\) and \(B_i\) denote the multiplicities of colour \(i\) on the two sides. A configuration is one-site blocked if and only if either (i) it is proper, meaning \(A_iB_i=0\) for every \(i\), or (ii) all \(q\) colours occur equally often on each side, meaning \(A_i=a/q\) and \(B_i=b/q\) for all \(i\). The second type exists precisely if \(q\mid a\) and \(q\mid b\) and has positive energy \(ab/q\). A configuration is two-site blocked if and only if it is proper.

Define \(P_{a,b}(q)\) to be the number of proper labelled \(q\)-colourings, and let \(Z^{(r)}_{a,b;q}(u)\) count all \(r\)-site-blocked states by the number of monochromatic edges. Then the **complete blocked-energy law** is
\[
\begin{aligned}
P_{a,b}(q)&=\sum_{s=1}^{q-1}\binom qs\,s!S(a,s)(q-s)^b,\\
Z^{(1)}_{a,b;q}(u)&=P_{a,b}(q)+\mathbf1_{q\mid a,\,q\mid b}\frac{a!b!}{[(a/q)!]^q[(b/q)!]^q}\,u^{ab/q},\\
Z^{(2)}_{a,b;q}(u)&=P_{a,b}(q).
\end{aligned}
\]
Here \(S(a,s)\) is a Stirling number of the second kind. When the divisibility condition fails, the second term is defined as zero; no factorial with a noninteger argument is used.

In the symmetric sequence \(a=b=n\), write \(B_{n,q}=Z^{(1)}_{n,n;q}(1)\), \(m_q=\lfloor q^2/4\rfloor\), and
\[
c_q=\begin{cases}\binom q{q/2},&q\text{ even},\\2\binom q{(q-1)/2},&q\text{ odd}.\end{cases}
\]
For each fixed \(q\ge3\), the two subsequences obey
\[
\begin{aligned}
B_{n,q}&\sim\frac{q^{2n+q}}{(2\pi n)^{q-1}},&&n\to\infty,\ q\mid n,\\
B_{n,q}&\sim c_qm_q^n,&&n\to\infty,\ q\nmid n.
\end{aligned}
\]
Consequently,
\[
\lim_{\substack{n\to\infty\\q\mid n}}\frac{\log B_{n,q}}{2n}=\log q,
\qquad
\lim_{\substack{n\to\infty\\q\nmid n}}\frac{\log B_{n,q}}{2n}=\frac12\log m_q.
\]
The two limits differ by at least \(\log2\). Thus the standard unrestricted-size blocked-state entropy density **does not exist**: adding a single vertex to each side can remove almost every high-energy blocked configuration.

Equivalently, a uniform random \(q\)-colouring is blocked with probability asymptotic to \(q^q/(2\pi n)^{q-1}\) along \(q\mid n\), but to \(c_q(m_q/q^2)^n\) along \(q\nmid n\). The high-energy states in the divisible subsequence constitute asymptotically all blocked states, yet none survives the addition of two-site recolouring moves.

## Assumptions and scope
The graph is finite, simple, unweighted, and complete bipartite with **both parts nonempty**. Colours are labelled \(1,\ldots,q\), with a fixed palette \(q\ge3\); no colour-population constraint is imposed. The energy is exactly
\[
H(\sigma)=\sum_{uv\in E(K_{a,b})}\mathbf1_{\sigma_u=\sigma_v}=\sum_{i=1}^q A_iB_i.
\]
A common positive coupling factor does not change stability. An allowed move recolours at most \(r\) *distinct vertices* simultaneously and may change them to arbitrary other palette colours. Only moves with **strictly negative energy change** are accepted; neutral recolourings are forbidden. The limit takes \(n\to\infty\) at fixed \(q\), and \(\log\) denotes the natural logarithm.

## Proof
**1. One-site classification.** Recolour an occupied colour \(i\) on the first side to \(j\). This changes \(H\) by \(B_j-B_i\). Thus in a one-site-blocked configuration every colour occupied on the first side has *minimum multiplicity* on the second side. By symmetry, every colour occupied on the second side has minimum multiplicity on the first side.

If \(H=0\), no move can reduce the nonnegative energy, so every proper colouring is blocked. Conversely suppose \(H>0\). Then some colour \(i\) occurs on both sides. As \(A_i>0\), the one-site condition makes \(B_i\) the minimum among all \(B_j\); because \(B_i>0\), **every** \(B_j>0\). Now every colour occurs on the second side, and the symmetric condition forces all \(A_j\) to equal their common minimum. Since \(a>0\), every \(A_j>0\). Finally, since every colour occurs on the first side, the first condition forces all \(B_j\) to coincide. Normalization \(\sum_j A_j=a\), \(\sum_j B_j=b\) gives \(A_j=a/q\), \(B_j=b/q\), requiring both divisibilities. Conversely equal multiplicities yield zero change for every single-vertex recolouring. Such a state has \(H=q(a/q)(b/q)=ab/q>0\).

**2. Two-site classification.** Every proper colouring is also two-site blocked since energy cannot become negative. Suppose instead one has an equal-multiplicity nonproper blocked state. Because \(q\ge3\) and every colour occurs on both sides, choose distinct colours \(i\ne j\), a first-side vertex of colour \(i\), and a second-side vertex of colour \(j\). Recolour these vertices simultaneously from \(i\) to \(j\) and from \(j\) to \(i\), respectively. Writing the changes of the two multiplicity vectors as \(\delta A=e_j-e_i\) and \(\delta B=e_i-e_j\), the energy change is
\[
\delta H=(\delta A)\cdot B+A\cdot(\delta B)+(\delta A)\cdot(\delta B)=0+0-2=-2.
\]
Thus no nonproper one-site-blocked state is two-site blocked. Any two-site-blocked state is necessarily one-site blocked, establishing the assertion.

**3. Exact energy enumeration.** To count proper configurations, choose exactly \(s\) colours present on the first side: \(\binom qs\) choices. There are exactly \(s!S(a,s)\) onto assignments to the \(a\) vertices on that side, and then \((q-s)^b\) choices on the other side. Sum over \(1\le s\le q-1\). To count equal-multiplicity states when \(q\mid a,b\), choose independent multinomial arrangements on the two labelled parts, giving \(\frac{a!}{[(a/q)!]^q}\frac{b!}{[(b/q)!]^q}\). These two types have distinct energies zero and \(ab/q\), so the enumerators follow without double-counting.

**4. Arithmetic entropy limits.** Fix \(q\ge3\) and take \(a=b=n\). For each fixed \(s\), the onto count satisfies \(s!S(n,s)=s^n(1+O(((s-1)/s)^n))\). Hence the largest bases among \(s(q-s)\), for \(1\le s<q\), are \(m_q\), achieved by the unique middle \(s=q/2\) when \(q\) is even and both middle values \(s=(q\pm1)/2\) when \(q\) is odd. Therefore \(P_{n,n}(q)\sim c_qm_q^n\) with exactly the stated \(c_q\). If \(q\nmid n\), this is the entire blocked count.

If \(q\mid n\), the nonproper count is \(M_{n,q}=[n!/((n/q)!)^q]^2\). Stirling's formula gives \(M_{n,q}\sim q^{2n+q}(2\pi n)^{1-q}\). Since \(m_q<q^2\), the proper term \(P_{n,n}(q)=O(m_q^n)\) is exponentially smaller than \(M_{n,q}\). Thus \(B_{n,q}\sim M_{n,q}\). Taking natural logarithms and dividing by \(2n\) gives the two subsequential limits. Because \(m_q\le q^2/4\), their difference is at least \(\log2\). Dividing the asymptotic counts by the total \(q^{2n}\) assignments gives the two blocked-probability laws. This completes the proof.

## Verification
The complete Python 3 standard-library checker `verify_potts_bipartite.py` independently constructs the original monochromatic-edge energy and directly tests every one-vertex recolouring and every allowed two-vertex recolouring. For \(q\in\{2,3,4\}\), it tests 50 choices of part sizes and 25,300 labelled configurations, comparing one-site stability with the claimed support/equipartition classification and the predicted exact counts. The two-site test examines 1,986 one-site-blocked configurations, and every comparison passed. Cases with \(q=2\) are an additional check of an extension of the same elementary proof, not part of the stated \(q\ge3\) novelty scope. The program also evaluates exact finite-size multinomial counts for several larger palette values as arithmetic spot checks. The all-size theorem is proved above, not inferred from enumeration.

Run `python3 verify_potts_bipartite.py` from the directory containing this document's standalone verifier. It needs no third-party libraries or external data.

## Relationship to prior work
Sokal's *Chromatic Polynomials, Potts Models and All That* (1999, arXiv:cond-mat/9910503v1) provides the standard correspondence between proper colourings and the zero-temperature antiferromagnetic Potts partition function. That is precisely the zero-energy term above, not a claim of novel ground-state counting. Salas and Shrock (2001, arXiv:cond-mat/0102190v1) calculate ground-state Potts partition functions on lattice tubes including a complete-bipartite transverse section; their calculations do not supply the one- versus two-site blocked energy spectrum here.

Kun, Powers and Reyzin, *Anti-Coordination Games and Stable Graph Colorings* (2013, arXiv:1308.3258v1), define **exactly the same one-vertex non-strict stability condition** as a stable graph colouring on an arbitrary graph. Thus neither that equilibrium notion nor the general local best-response inequality is new. Their inspected general results concern equilibrium existence, computational complexity and price of anarchy; they do not state the complete-bipartite energy-resolved enumeration, the exact simultaneous two-recolouring collapse, or the arithmetically nonconvergent blocked entropy. These conclusions follow here from additional two-sided support rigidity and exact asymptotic counting; a differently indexed prior application of their framework remains possible.

The public result *Majority C-colorings of complete multipartite graphs* (2026) counts equal binary splits in multipartite parts under a **same-colour-majority** rule. Its half-split configurations coincide with the \(q=2\) equal-count slice here, but its inequality points in the **opposite direction** from anti-coordination and it does not classify arbitrary-paletted antiferromagnetic blocked configurations, the proper-colouring branch, or the two-site collapse. De Berganza and collaborators (2006, arXiv:cond-mat/0610039v1) investigate a different kinetic Potts model on a square lattice, rather than this finite complete-bipartite blocked-state count.

## Limitations
The conclusions are exact for the stipulated **strictly downhill** update rule. A dynamics that accepts energy-neutral moves need not trap the equal-multiplicity configurations, and no physical relaxation-time, quench probability, or finite-temperature thermodynamic transition is inferred. The asymptotic statements require a fixed number of palette colours and symmetric part sizes. The normalised blocked-state entropy is a combinatorial count, not the equilibrium Potts free energy. The general one-site anti-coordination characterization is prior work, and a previously unindexed exact complete-bipartite specialization remains an originality risk. There is no independent scientific audit.

## References
1. A. D. Sokal, *Chromatic Polynomials, Potts Models and All That*, arXiv:cond-mat/9910503v1, first submitted 1999-10-30.
2. J. Salas and R. Shrock, *Exact T=0 Partition Functions for Potts Antiferromagnets on Sections of the Simple Cubic Lattice*, arXiv:cond-mat/0102190v1, first submitted 2001-02-10.
3. J. Kun, B. Powers and L. Reyzin, *Anti-Coordination Games and Stable Graph Colorings*, arXiv:1308.3258v1, first submitted 2013-08-14.
4. M. Ibáñez de Berganza et al., *Phase Separation of the Potts Model in the Square Lattice*, arXiv:cond-mat/0610039v1, first submitted 2006-10-02.
5. *Majority C-colorings of complete multipartite graphs*, public research record, 2026-10-04; especially the exact half-split construction for two colours.
