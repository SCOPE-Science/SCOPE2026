# The 540 indispensable quartic trades of the cubic-surface tritangent configuration

## Finding

Let \(S\) be a smooth cubic surface over an algebraically closed field \(k\) of characteristic zero. Its 27 lines and 45 tritangent planes define the **tritangent incidence toric ideal** \(I\): take one variable \(z_T\) for each tritangent \(T\) and map it to the product of three independent variables corresponding to the lines in \(T\). The kernel is a homogeneous prime binomial ideal in 45 variables.

There are **no degree-two binomial relations**. In degree three, \(I\) has exactly 120 indispensable binomials, the classical exchanges between pairs of Steiner trihedra. In degree four, \(I\) has **exactly 540 further indispensable binomials modulo its degree-three generators**. Each quartic is a trade between two disjoint quadruples of distinct tritangent planes covering the same twelve lines, and all 540 quartics form a **single orbit under \(W(E_6)\)**. Thus a minimal homogeneous binomial generating set must contain 120 cubics and 540 quartics. No assertion is made about generators of degree five or above.

In particular the classical 120 Steiner exchanges alone do **not** generate \(I\). This is a statement about the defined 45-variable incidence *monomial* algebra, not about the distinct 27-generator Cox ring or its quadratic presentation.

## Assumptions and scope

Choose the standard model of \(S\) as the blowup of \(\mathbb P^2\) at six general points indexed by \(0,\ldots,5\). Denote the 27 lines by \(E_i\), \(L_{ij}=H-E_i-E_j\) with \(i<j\), and \(Q_i=2H-\sum_{j\ne i} E_j\). The 45 tritangent triples are precisely
\[
\{E_i,L_{ij},Q_j\}\quad(i\ne j),\qquad
\{L_{ij},L_{kl},L_{mn}\}\quad\text{for partitions of six indices into pairs}.
\]
Let \(R=k[z_T:T\in\mathcal T]\), \(U=k[x_\ell:\ell\in\mathcal L]\), and \(\phi:R\to U\) send \(z_T\) to \(\prod_{\ell\in T}x_\ell\). Set \(I=\ker\phi\). All degrees below refer to the number of tritangent variables, not to anticanonical divisor degree.

## Proof

**Step 1: Exact finite incidence model.** The displayed sets give 30 mixed tritangents and 15 matchings, so 45 in all; the sum of line divisor classes for every triple is \(-K_S=3H-\sum E_i\). Standard cubic-surface line geometry identifies these with all tritangent planes. For each degree-\(d\) tritangent monomial \(M\), let \(\sigma(M)\in\mathbb N^{27}\) count the 27 lines occurring in its tritangent factors. Two monomials have the same image under \(\phi\) exactly when their signatures agree. Therefore every homogeneous kernel relation is spanned by binomial differences within a signature fiber.

**Step 2: Exhaustive fiber counts.** Enumerate multisets of size \(d\) from the 45 distinct tritangents, including repeated factors. The exact census, independently repeatable using the accompanying verifier, is:

| \(d\) | Number of monomials | Singleton fibers | Doubleton fibers | Larger fibers |
| --- | ---: | ---: | ---: | ---: |
| 2 | 1,035 | 1,035 | 0 | 0 |
| 3 | 16,215 | 15,975 | 120 | 0 |
| 4 | 194,580 | 182,700 | 5,940 | 0 |

The algorithm forms each length-27 signature by exact integer addition and groups equal tuples; it has no numerical tolerance, probabilistic step, or unenumerated remainder. In particular the only cubic relations are the 120 two-element fibers; these are the well-known Steiner-trihedral exchanges.

**Step 3: Exact quartic minimality.** Among the 5,940 quartic doubleton fibers, 5,400 have a shared tritangent variable in their two monomials. Canceling that variable produces a cubic relation, since no degree-two relation exists. Conversely each of the 120 cubic pairs multiplied by each of the 45 variables yields such a pair. The resulting 5,400 pairs are distinct: a duplicated lift would give a quartic fiber with at least three monomials or an equality with two common factors, implying a degree-two relation. The remaining 540 doubleton pairs have relatively prime monomials, each supported on four distinct tritangent variables. In a fixed doubleton fiber, lower-degree generators can connect the two monomials only after multiplication by a common variable; none exists. Therefore the unique binomial difference of each such pair is indispensable in *every homogeneous binomial generating set*. Conversely all other quartic relations follow from the cubic relations, so precisely 540 new minimal degree-four generators occur.

**Step 4: A single \(E_6\) orbit.** Represent line classes as integer vectors in the basis \((H,E_0,\ldots,E_5)\), with intersection form \(d\cdot e=d_H e_H-\sum d_i e_i\). For the six simple roots \(\alpha_0=H-E_0-E_1-E_2\) and \(\alpha_{i+1}=E_i-E_{i+1}\), \(0\le i\le4\), act by the reflections \(s_\alpha(d)=d+(d\cdot\alpha)\alpha\). Each reflection permutes the 27 line classes, hence the 45 triples and all 540 quartic pairs. Starting from the pair with deterministic tritangent indices \((0,6,12,15)\leftrightarrow(2,5,11,17)\), breadth-first closure under the six displayed reflections contains all 540 indispensable quartics. Thus they form one \(W(E_6)\)-orbit. This finite closure is checked independently of any orbit-stabilizer formula.

## Verification

Run `python3 verify.py` with standard Python 3 (no additional dependencies). The verifier constructs the 27 divisor classes and 45 tritangents from scratch, verifies all anticanonical sums, enumerates all multisets of tritangents in degrees two through four, checks the exact histograms and the 5,400 degree-three lifts, verifies coprimality of all remaining 540 pairs, and computes the entire \(W(E_6)\) orbit using simple-root reflections. The code raises an exception on any mismatch. Its successful output ends with `WEYL_OK: all 540 indispensable quartics form one W(E6) orbit`.

## Relationship to prior work

Elsenhans--Jahnel's treatment of Steiner trihedra explicitly describes all 120 pairs of Steiner trihedra and the \(W(E_6)\) symmetry. Their cubic exchanges are *prior mathematics*, not part of the new contribution. Their papers on Galois descent and Brauer classes do not report an incidence toric-ideal minimal Markov layer of 540 quartics. Sturmfels--Xu study Cox--Nagata rings and toric initial ideals in 27 generators; their cubic-surface toric model is generated by 81 quadrics, but its defining map, variables and grading are not the 45-tritangent monomial map above. Thus their quadratic-generation theorem does not imply the statement here. No equivalent 540-quartic incidence presentation was located in the inspected sources; this is a bounded priority assessment, not a proof of absolute novelty.

## Limitations

The result determines the minimal generator layers up through degree four only. It does not claim that the 660 binomials generate the full toric ideal, nor determine higher-degree Markov moves, Gröbner bases, normality, or the Hilbert series. The universal geometry concerns the 27-line configuration on smooth cubic surfaces over algebraically closed characteristic-zero fields; special degenerate cubic surfaces are outside scope. An unknown older equivalent formulation of the quartic trade orbit remains a priority risk.

## References

1. A.-S. Elsenhans and J. Jahnel, *Cubic surfaces with a Galois invariant pair of Steiner trihedra*, arXiv:1006.1474 (first posted 2010-06-08), https://arxiv.org/abs/1006.1474.
2. A.-S. Elsenhans and J. Jahnel, *On the order three Brauer classes for cubic surfaces*, arXiv:1110.2086 (first posted 2011-10-10), https://arxiv.org/abs/1110.2086.
3. B. Sturmfels and Z. Xu, *Sagbi Bases of Cox-Nagata Rings*, arXiv:0803.0892 (first posted 2008-03-06), https://arxiv.org/abs/0803.0892.
