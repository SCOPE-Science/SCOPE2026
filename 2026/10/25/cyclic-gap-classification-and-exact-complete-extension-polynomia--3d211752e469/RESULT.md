# Cyclic-gap classification and exact complete-extension polynomial of bidirected argumentation cycles

## Finding

For every integer \(n\ge3\), let \(F_n=(V_n,R_n)\) be the labelled Dung argumentation framework with \(V_n=\mathbb Z/n\mathbb Z\). Its attacks are both directions of each edge of the simple cycle, with no self-attacks. Write \(\mathrm{CO}(F_n)\) for its complete extensions and define
\[
P_n(u)=\sum_{S\in\mathrm{CO}(F_n)}u^{|S|},\qquad
G(z)=z^2+z^3+\frac{z^5}{1-z}.
\]

**Theorem (exact complete-extension spectrum).** A subset \(S\subseteq V_n\) is complete precisely if it is empty or its positive clockwise gaps between consecutive selected vertices all belong to \(\{2,3,5,6,7,\ldots\}\). In particular, gap \(4\) is forbidden, even though it is allowed for an arbitrary independent set.

The exact size-refined generating function, valid as a formal power series in \(z\) with polynomial coefficients in \(u\), is
\[
\boxed{\sum_{n\ge3}P_n(u)z^n
=\frac{z^3}{1-z}+\frac{zuG'(z)}{1-uG(z)}-2uz^2.}
\]
Equivalently, setting \(c_{n,k}=[u^k]P_n(u)\), one has \(c_{n,0}=1\) and
\[
\boxed{c_{n,k}=\frac nk[z^n]G(z)^k\quad
(1\le k\le\lfloor n/2\rfloor),}
\]
with all remaining coefficients zero. Specializing \(u=1\) gives
\[
\boxed{\sum_{n\ge3}|\mathrm{CO}(F_n)|z^n
=\frac{z^3(4-z+4z^2-2z^3+3z^4)}
{1-z-z^2+z^4-z^5}.}
\]
The counts for \(n=3,4,\ldots,16\) are
\[
4,3,11,12,22,35,49,83,122,192,300,458,719,1107.
\]
For \(n\ge8\), the totals \(c_n=|\mathrm{CO}(F_n)|\) satisfy
\[
c_n=c_{n-1}+c_{n-2}-c_{n-4}+c_{n-5}.
\]
Moreover, let \(r\in(0,1)\) be the unique real solution of \(G(r)=1\) and put \(\rho=r^{-1}\approx1.549906072594\). Then
\[
\boxed{|\mathrm{CO}(F_n)|\sim\rho^n.}
\]
The leading multiplicative constant is exactly \(1\). The stable (equivalently, preferred) extensions are exactly the nonempty selected sets with gaps \(2\) or \(3\), and their count is asymptotic to \(\pi^n\), where \(\pi\approx1.324717957245\) is the plastic constant. Consequently, the proportion of complete extensions that are stable is asymptotic to \((\pi/\rho)^n\), with \(\pi/\rho\approx0.854708540517\).

## Assumptions and scope

The attack graph is precisely the loop-free bidirected simple cycle. Labels distinguish its \(n\) vertices; sets, not cyclic-rotation equivalence classes, are counted. Dung's standard semantics are used: a set is conflict-free if it contains no mutually attacking pair; it defends a vertex if it attacks every attacker of that vertex; and a complete extension is conflict-free, defends each of its elements, and contains every vertex it defends. No assumptions on an atom valuation or probabilistic distribution are made. The displayed generating series begins at \(n=3\); the correction term \(-2uz^2\) excludes a formal two-vertex contribution arising from the ordinary cyclic-composition construction.

## Proof

**1. Independent-set and defence reduction.** In a symmetric attack graph every conflict-free set \(S\) defends each of its own vertices: any attacker \(x\) of \(v\in S\) is itself attacked by \(v\). Thus admissibility is exactly conflict-freeness (also recorded by Coste-Marquis, Devred and Marquis). Let \(N(S)\) be the open neighborhood of \(S\); for a conflict-free \(S\), its canonical labelling has \(S\) labelled in, \(N(S)\) labelled out, and \(U=V_n\setminus(S\cup N(S))\) labelled undecided. Every out-vertex has an in-neighbor and therefore is not defended, since an independent \(S\) does not attack any of its elements. A vertex \(v\in U\) is defended by \(S\) precisely when *all* its neighbors lie in \(N(S)\), which is equivalent to \(v\) being isolated in the induced graph on \(U\). It follows that \(S\) is a complete extension if and only if \(S\) is independent and \(U\) has no isolated vertices. In particular, \(S=\varnothing\) is complete because the underlying cycle has no isolated vertices.

**2. Gap classification.** For nonempty independent \(S\), order its \(k\) vertices clockwise and let \(d_1,\ldots,d_k\) be their positive cyclic gaps, so each \(d_i\ge2\) and \(\sum_i d_i=n\). Between two selected vertices at distance \(d_i\), the immediate neighbors are out. The interior undecided run has length \(\max\{d_i-3,0\}\). When \(d_i=2\) or \(3\) this run is empty; when \(d_i=4\) it is a single isolated undecided vertex; and when \(d_i\ge5\) it has at least two vertices, so every undecided vertex has an undecided neighbor. For \(k=1\), the same argument applies to the single wraparound gap of length \(n\); it is obtained by walking once around the cycle rather than reducing the gap modulo \(n\). Distinct gaps produce disjoint undecided runs and cannot contribute edges between runs because a selected vertex and its out-neighbors separate them. Hence the absence of undecided isolates is equivalent to all gaps belonging to \(\{2,3\}\cup\{5,6,\ldots\}\), as claimed.

**3. Exactly counting selected sizes.** Each allowed clockwise gap contributes a monomial in \(G(z)=z^2+z^3+\sum_{d\ge5}z^d\). An ordered tuple of \(k\) gaps adding to \(n\), together with a chosen starting labelled vertex, determines a complete extension plus a distinguished selected vertex. There are \(n[z^n]G(z)^k\) such pairs, whereas each nonempty complete extension of size \(k\) admits exactly \(k\) choices of its distinguished selected vertex. Division by \(k\) proves the coefficient formula. The bound \(k\le\lfloor n/2\rfloor\) follows from \(d_i\ge2\). The empty set contributes one for each \(n\ge3\), giving \(z^3/(1-z)\).

Summing over positive \(k\) as formal series gives
\[
\sum_{k\ge1}\frac{n}{k}u^k[z^n]G(z)^k
=[z^n]\,zu\frac{G'(z)}{1-uG(z)}
\]
after weighting by \(u^k\) and applying \(z\,d/dz\). The formal construction also creates \(2\) one-element sets when \(n=2\), although the simple cycle family begins at \(n=3\); subtraction of \(2uz^2\) produces the asserted full series. Simplifying at \(u=1\) gives its stated rational function. Multiplying by the denominator proves the recurrence from \(n=8\) onward.

**4. Dominant singularity and stable contrast.** The real function \(G\) has strictly positive derivative on \((0,1)\), starts at zero, and diverges as its argument approaches one. Therefore there is a unique \(r\in(0,1)\) with \(G(r)=1\). For \(|z|<r\) the nonempty-extension series has no singularities because \(|G(z)|\le G(|z|)<1\). On \(|z|=r\), equality \(G(z)=1\) forces both \(z^2\) and \(z^3\) to have phase one, and hence \(z=r\); no other point on the circle is singular. Near \(r\), one has
\[
\frac{zG'(z)}{1-G(z)}=\frac{1}{1-z/r}+O(1).
\]
Because the remaining part \(z^3/(1-z)-2z^2\) is analytic at \(r\), standard simple-pole coefficient transfer yields \(c_n\sim r^{-n}\) with leading constant \(1\). For a stable extension, every non-selected vertex must be adjacent to a selected one; thus only gaps \(2\) and \(3\) remain, giving the same marked-gap construction with \(G_{\mathrm{st}}(z)=z^2+z^3\). Its unique positive singularity is \(1/\pi\), where \(\pi^3=\pi+1\), and its leading pole residue likewise yields stable count asymptotic to \(\pi^n\). On symmetric graphs stable and preferred extensions coincide, as known; division establishes the exponentially vanishing stable fraction among complete extensions.

## Verification

The accompanying standalone Python 3 program `checker.py` independently implements the definition of defence and completeness. For every labelled cycle of orders \(3\) through \(16\), it examines all \(2^n\) subsets, totaling \(131064\) subsets, and checks that the complete-extension size distribution agrees simultaneously with the cyclic-gap condition and with coefficient convolution of \(G(z)^k\). It independently checks the stable-extension gap enumeration and numerically locates the positive root of \(G(r)=1\). A successful run prints `ALL_CHECKS_OK`. These exhaustive finite checks do not establish the infinite result; the symbolic reduction and generating-series proof above do.

## Relationship to prior work

Dung's complete semantics and the equivalence between conflict-freeness and admissibility for symmetric irreflexive frameworks predate this finding; in particular, Coste-Marquis, Devred and Marquis establish that equivalence and the coincidence of stable and preferred semantics in their 2005 article. Rodrigues (2017) develops legal three-valued labellings and an algorithm for generating complete extensions, including cycle-shaped benchmarks; this supplies relevant algorithmic background but not an all-length size-refined cycle polynomial. Obiedkov and Sertkaya (2026) show how complete, stable and preferred extensions can be computed by enumerating suitable closed sets. Their algorithms operate on arbitrary argumentation frameworks, rather than deriving the explicit all-size cycle gap classification and rational counting law. The distinguished-vertex cyclic-composition method here uses prior semantics to derive a new exact enumerator and asymptotic ratio for this family.

## Limitations

The formula counts labelled simple cycles with reciprocal neighboring attacks only; it does not extend as stated to directed one-way cycles, chords, self-attacks, or arbitrary symmetric graphs. A generic enumeration algorithm can recover the values at any fixed order, but is not an explicit all-orders formula. The mathematical originality comparison is to inspected sources, not a proof that an equivalent enumerator has never appeared under three-state spin-system, independent-set, or cellular-labelling terminology. The proof is theoretical; the checker tests finitely many orders. No independently conducted external validation is asserted.

## References

- P. M. Dung, “On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games,” *Artificial Intelligence* 77 (1995), 321–357.
- S. Coste-Marquis, C. Devred and P. Marquis, “Symmetric Argumentation Frameworks,” ECSQARU (2005). Open PDF: https://www.cril.univ-artois.fr/~marquis/coste-devred-marquis-ecsqaru05.pdf
- O. Rodrigues, “A Forward Propagation Algorithm for the Computation of the Semantics of Argumentation Frameworks,” TAFA (2017). Open preprint: https://homepages.abdn.ac.uk/n.oren/pages/TAFA-17/papers/TAFA-17_paper_6.pdf
- S. Obiedkov and B. Sertkaya, “Computing Extensions of Abstract Argumentation Frameworks by Enumerating Closed Sets,” KR (2026), 512–522. https://doi.org/10.24963/kr.2026/49 ; open PDF: https://proceedings.kr.org/2026/49/kr2026-0049-obiedkov-et-al.pdf
