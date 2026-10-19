# Sharp nonbinary de Bruijn next-window probabilities and their unique extremizers

## Finding

**Theorem.** Fix integers \(q\geq3\) and \(n\geq2\), and a labelled alphabet \(\Sigma\) of size \(q\). Choose a cyclic order-\(n\) de Bruijn word uniformly among all such words up to rotation. For any nonconstant \(w\in\Sigma^{n+1}\), let \(p_{q,n}(w)\) be the probability that \(w\) occurs as a cyclic contiguous factor. Then

\[
\frac{q-2}{q(q-1)}\;\leq\;p_{q,n}(w)\;\leq\;\frac1{q-1}.
\]

The upper equality holds **if and only if** \(w=a^n b\) or \(w=b a^n\) for two distinct symbols \(a,b\); thus exactly \(2q(q-1)\) words attain the maximum for each \(n\). The lower equality holds **if and only if** \(n=2\) and \(w=aba\) for \(a\ne b\); thus exactly \(q(q-1)\) words attain the global sharp lower bound at order two, and for all \(n>2\) the inequality is strict. Constant \(w\) have probability zero and are excluded from the inequality.

In particular, the uniform positive lower bound does **not** deteriorate with the de Bruijn order. For \(t\) independent uniformly sampled cycles, the probability of missing some nonconstant length-\(n+1\) word in their union is at most \((q^{n+1}-q)(1-(q-2)/(q(q-1)))^t\).

## Assumptions and scope

The word \(w\) occurs if one of the \(q^n\) circular start positions has its length-\(n+1\) factor equal to \(w\). Rotation is identified but symbol labels are not permuted; each length-\(n\) word occurs precisely once. The theorem concerns single-factor inclusion, not simultaneous-factor independence. It requires \(q\geq3\); binary cycles have additional impossible nonconstant next-order factors, so no analogous strictly positive all-pattern bound exists.

For an explicit intermediate formula, write \(m=n-1\), and form the length-\(m\) blocks \(a=w_1\cdots w_m\), \(b=w_2\cdots w_{m+1}\), \(c=w_3\cdots w_{m+2}\). Here lowercase \(a,b,c\) denote *blocks*, distinct from the symbol letters used in the theorem. For length-\(m\) blocks \(x,y\), define the overlap indicator

\[
I_k(x,y)=\mathbf 1\{x_{k+1}\cdots x_m=y_1\cdots y_{m-k}\},\qquad 0\le k<m.
\]

(The empty-border convention is not needed because \(k<m\).) Define

\[
d_k=I_k(b,a)-I_k(b,b)-I_k(c,a)+I_k(c,b).
\]

For every nonconstant \(w\), the following exact counting identity holds:

\[
p_{q,n}(w)=\frac1{q-1}\left(1+\sum_{k=0}^{m-1}\frac{d_k}{q^{k+1}}\right).
\tag{1}
\]

This determinant-free specialization of conditional path-count identities is used as a *lemma* to prove the extremal theorem, not asserted to supersede classical general path-counting formulas.

## Proof

**Step 1: a consecutive-arc count.** Let \(G\) be the directed order-\(m\) de Bruijn graph. Its vertices are \(\Sigma^m\); each length-\(m+1\) word is one uniquely labelled arc, and all in/out degrees are \(q\). Every cyclic de Bruijn word corresponds to an Euler circuit of \(G\). A nonconstant \(w\) prescribes two **distinct** consecutive arcs \(e:a\to b\) and \(f:b\to c\). (Their equality would require \(w\) constant.) Replace these two arcs with one *labelled* macro-arc \(a\to c\) to form \(H\). The replacement is reversible in edge-labelled Euler circuits, including when the new arc is parallel to another arc. Every vertex of \(H\) has degree \(q\), except \(b\), which has degree \(q-1\). In particular, all degrees remain positive since \(q\geq3\).

Write \(\tau(K)\) for the number of in-arborescences toward a fixed root of a balanced Eulerian directed multigraph \(K\); the count is root-independent. The directed BEST theorem, using labelled edges and Euler circuits up to cyclic rotation, gives

\[
p_{q,n}(w)=\frac{\tau(H)}{(q-1)\tau(G)}.
\tag{2}
\]

If \(H\) is disconnected, both sides are zero under the matrix-tree convention.

**Step 2: exact overlap formula.** Let \(A\) be the adjacency matrix of \(G\) and \(L=qI-A\) its row Laplacian. Denote coordinate vectors by \(e_x\). Removing the two arcs and adding the macro-arc changes the Laplacian by the rank-one matrix

\[
L(H)-L(G)=(e_a-e_b)(e_b-e_c)^\mathsf T.
\]

The directed Matrix-Tree theorem and the matrix determinant lemma give

\[
\frac{\tau(H)}{\tau(G)}=1+(e_b-e_c)^\mathsf T x,
\qquad Lx=e_a-e_b.
\tag{3}
\]

The scalar is independent of the additive constant of \(x\). For every pair of vertices, \((A^k)_{xy}=I_k(x,y)\) if \(0\leq k<m\), and \(A^m\) is the all-ones matrix: exactly one walk of length \(m\) connects any two length-\(m\) blocks. Hence a solution is

\[
x=\sum_{k=0}^{m-1}q^{-k-1}A^k(e_a-e_b),
\]

because \(A^m(e_a-e_b)=0\). Substitution in (2)--(3) proves (1). A constant length-\(n+1\) word would use the same loop arc twice, impossible in an Euler circuit, so its probability is zero.

**Step 3: identify first coefficients.** For nonconstant \(w\), direct evaluation at \(k=0\) gives

\[
d_0=\mathbf1\{a=b\}-1-\mathbf1\{c=a\}+\mathbf1\{c=b\}.
\]

Here \(a=b\) holds precisely when the first \(n\) letters of \(w\) are constant, and \(c=b\) precisely when the last \(n\) letters are constant. Such two events cannot both happen for nonconstant \(w\). Also \(c=a\) means \(w\) alternates between two distinct symbols (period two). Therefore \(d_0=0\) exactly in the two boundary-run families \(w=s^nt\) and \(w=ts^n\), \(s\ne t\); \(d_0=-2\) exactly in the alternating family; and \(d_0=-1\) otherwise. In each boundary-run family all remaining \(d_k\) vanish too, so (1) gives \(p_{q,n}(w)=1/(q-1)\).

**Step 4: sharp upper bound and uniqueness.** Every indicator is zero or one, so \(-2\leq d_k\leq2\). For any nonconstant \(w\) outside the boundary-run families, \(d_0\leq-1\); hence, since \(m\) is finite,

\[
\sum_{k=0}^{m-1}\frac{d_k}{q^{k+1}}
\leq-\frac1q+\frac{2}{q(q-1)}\left(1-q^{-(m-1)}\right)<0
\quad(q\geq3).
\]

(The right-hand expression is negative for \(q=3\) because its final factor is strictly below one, and is negative a fortiori for larger \(q\).) Equation (1) proves the strict upper bound outside the stated families and proves the number of maximizers.

**Step 5: sharp lower bound and uniqueness.** If \(d_0=-1\), the opposite geometric bound gives

\[
\sum_{k=0}^{m-1}\frac{d_k}{q^{k+1}}
\geq-\frac1q-\frac{2}{q(q-1)}\left(1-q^{-(m-1)}\right).
\]

Consequently

\[
p_{q,n}(w)>\frac{q^2-2q-1}{q(q-1)^2}
\geq\frac{q-2}{q(q-1)},
\]

where the second comparison is equality only when \(q=3\) and the first remains strict. If \(d_0=0\), the already established upper equality is strictly greater than the claimed lower endpoint for \(q\geq3\).

It remains to treat \(d_0=-2\), namely alternating two-symbol words. Their overlap indicators satisfy \(d_k=2(-1)^{k+1}\); summing the finite geometric progression in (1) yields

\[
p_{q,n}(w)=\frac{q-1+2(-1/q)^m}{q^2-1}.
\tag{4}
\]

For odd \(m\), the negative correction \(-2/q^m\) is minimal uniquely at \(m=1\); for even \(m\), the correction is positive. Thus (4) is at least \((q-2)/(q(q-1))\), with equality if and only if \(m=1\), i.e. \(n=2\). There are \(q(q-1)\) alternating triples \(sts\), \(s\ne t\). This completes the sharp bounds and both equality classifications. The sampling bound follows by a union bound over all \(q^{n+1}-q\) nonconstant patterns.

## Verification

Run `python3 verify.py` next to `verification_output.txt` using Python 3 standard library. The checker enumerates all local successor permutations, checks which are one Euler circuit, and independently tests the formula against exact Matrix-Tree determinants after two-arc contraction. It also enumerates the nonconstant words in multiple alphabet/order pairs and checks both sharp bounds, their equality cases, and the strict lower bound for every tested order above two. All recorded tests passed. The finite checks corroborate but do not prove the all-parameter theorem, which rests on Steps 1--5.

## Relationship to prior work

Sawada and Gabrić (2025) develop uniformly random generation of de Bruijn cycles via arborescences, motivating quantitative questions about local words. The BEST theorem and Matrix-Tree theorem are classical. Cowan (1991, Theorem in Section 3) already gives exact expected frequencies of any specified pattern conditional on the transition-count matrix for finite-state Markov chains; by recoding higher-order blocks, that theory gives the individual next-window marginal implicitly as a ratio of general counts. Dawson and Good (1957) and Rødland (2006) develop broader frequency-count frameworks. **No novelty is claimed for the general conditional expected-count principle, the determinant ratio alone, or the already known existence/support classification.** The claim assessed here is the simultaneous order-independent sharp **two-sided extremal bound and complete equality classification**, obtained by exploiting the special overlap geometry across all de Bruijn orders. The inspected works do not state these inequalities or all extremizers.

## Limitations

Only one next-order factor at a time is constrained; correlations between distinct factors and nonuniform sampling are not determined. The binary case does not satisfy the asserted positive lower bound. Earlier general exact counting formulas can be specialized to compute any fixed marginal and thus may allow an alternative derivation of this extremal optimization; independently establishing priority requires broader mathematical literature comparison. The full text of the 2006 Rødland paper was not available during this review, so a more implicit equivalent optimization cannot be ruled out. The 1957 Dawson--Good article was available only through bibliographic/abstract evidence, not examined fully.

## References

1. J. Sawada and D. Gabrić, *Random generation of universal cycles and de Bruijn sequences* (first public version 2025-10-18), arXiv:2510.16545, https://arxiv.org/abs/2510.16545. Later version titled *Las Vegas algorithms to generate universal cycles and de Bruijn sequences uniformly at random*.
2. R. Cowan, *Expected frequencies of DNA patterns using Whittle's formula*, Journal of Applied Probability **28** (1991), 886--892, https://doi.org/10.2307/3214691; author archived full text https://ssh.maths.usyd.edu.au/u/richardc/Whittleformula.pdf.
3. R. Dawson and I. J. Good, *Exact Markov probabilities from oriented linear graphs*, Annals of Mathematical Statistics **28** (1957), 946--956, https://www.jstor.org/stable/2237055.
4. E. A. Rødland, *Exact distribution of word counts in shuffled sequences*, Advances in Applied Probability **38** (2006), 116--133, https://doi.org/10.1239/aap/1143936143.
5. G. Tesler, *Multi de Bruijn Sequences* (2017), arXiv:1708.03654, https://arxiv.org/abs/1708.03654.
