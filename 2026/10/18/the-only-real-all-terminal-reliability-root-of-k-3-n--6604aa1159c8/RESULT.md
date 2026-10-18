# The only real all-terminal reliability root of \(K_{3,n}\)

## Finding

**Theorem.** Let \(n\ge 2\) be any integer. For the finite simple complete bipartite graph \(K_{3,n}\), let \(R_n(q)\) be its all-terminal reliability polynomial with independent edge-failure variable \(q\). Then \(q=1\) is its **only real zero**, of multiplicity exactly \(n+2\). Its other \(2n-2\) complex zeros, counted with multiplicity, are nonreal. Equivalently, the reduced polynomial

\[
H_n(q)=\frac{R_n(q)}{(1-q)^{n+2}}
\]

is strictly positive at every real \(q\) and has degree exactly \(2n-2\).

This result is a real-zero classification, **not** a newly claimed enumeration of the reliability polynomial. A previously published expression for the latter is credited below.

## Assumptions and scope

A graph is finite, simple and undirected. Each edge is independently operational with probability \(1-q\), and all vertices are operational. For \(0\le q\le1\), \(R_n(q)\) is the probability that the operational spanning subgraph is connected; polynomial evaluation defines \(R_n(q)\) for all real or complex \(q\). The theorem quantifies over all integers \(n\ge2\) and all real \(q\); roots are counted algebraically with multiplicity. No claim is made that the nonreal roots are distinct.

The graph has \(n+3\) vertices and \(3n\) edges. Its cycle rank, which equals the degree of the reduced reliability polynomial, is \(2n-2\).

## Proof

Write \(U=\{u_1,u_2,u_3\}\) for the part of size three and \(W\) for the other part. Every \(w\in W\) must retain at least one operational incident edge for connectivity. The probability of that event at an individual vertex is \(1-q^3\). Once every such vertex has a live edge, the graph is disconnected exactly when the induced connectivity relation on \(U\) is nontrivial; for three distinguished vertices this means that at least one distinguished vertex is separated from the other two.

For a fixed \(u_i\), separation from the other two requires every \(w\in W\) to have either exactly its edge to \(u_i\) operational, or its edge to \(u_i\) failed and at least one of its other two edges operational. The one-vertex probability is

\[
(1-q)q^2+q(1-q^2)=(1-q)q(1+2q).
\]

Any intersection of two such separation events requires each \(w\) to have exactly one operational incident edge, with probability \(3(1-q)q^2\). The triple intersection is the same event. Inclusion-exclusion over the three separated-hub events therefore yields the exact polynomial identity

\[
\begin{aligned}
R_n(q)&=(1-q^3)^n-3\big((1-q)q(1+2q)\big)^n
                +2\big(3(1-q)q^2\big)^n\\
&=(1-q)^n F_n(q),\\
F_n(q)&=(1+q+q^2)^n-3\big(q(1+2q)\big)^n+2(3q^2)^n.
\end{aligned}
\]

The inclusion-exclusion identity is first justified for real probabilities \(0\le q\le1\), and hence holds identically as a polynomial at every real or complex \(q\). This formula agrees with the previously published complete-bipartite reliability expression in Brown, Koç and Kooij (2014), after changing from edge-operation probability \(p\) to failure probability \(q=1-p\).

Set \(A=1+q+q^2\), \(B=q(1+2q)\), and \(C=3q^2\). Then \(A>0\) and \(C\ge0\) for every real \(q\), and the decisive exact identity is

\[
A+2C-3B=(1-q)^2.
\]

**Case 1: \(B\ge0\).** Here all three quantities \(A,B,C\) are nonnegative. By convexity of \(x\mapsto x^n\) on the nonnegative reals,

\[
\frac{A^n+2C^n}{3}\ge \left(\frac{A+2C}{3}\right)^n.
\]

For \(q\ne1\), the identity above and monotonicity of the power function imply \((A+2C)/3>B\). Hence \(A^n+2C^n>3B^n\), so \(F_n(q)>0\).

**Case 2: \(B<0\).** This occurs precisely when \(-\tfrac12<q<0\). If \(n\) is odd then \(-3B^n>0\), and hence \(F_n(q)>0\). If \(n\) is even, put \(x=-q\in(0,\tfrac12)\). Then

\[
A-3|B|=1-4x+7x^2
 =7\left(x-\frac27\right)^2+\frac37>0.
\]

Consequently \(A^n>(3|B|)^n\ge3|B|^n\); adding \(2C^n\ge0\) proves \(F_n(q)>0\) again.

Thus \(F_n(q)>0\) for every real \(q\ne1\). At \(q=1\), direct differentiation of the displayed powers gives

\[
F_n(1)=F_n'(1)=0,
\qquad F_n''(1)=6n^2 3^{n-2}>0.
\]

The zero of \(F_n\) at \(q=1\) therefore has multiplicity exactly two. Define the polynomial \(H_n(q)=F_n(q)/(1-q)^2\). It is positive at all real \(q\ne1\), and its value at \(q=1\) is \(F_n''(1)/2=3n^2 3^{n-2}>0\). Therefore \(H_n\) has no real zeros at all.

Finally, \(F_n\) has degree \(2n\): its leading coefficient is \(1-3\cdot2^n+2\cdot3^n>0\) for \(n\ge2\). Dividing by \((1-q)^2\) yields \(\deg H_n=2n-2\). Since \(R_n=(1-q)^{n+2}H_n\), all conclusions follow. \(\square\)

## Verification

Run `python3 verify_k3n_reliability.py` with Python 3.8 or later; it uses only the standard library. The program independently counts connected spanning edge subsets of \(K_{3,n}\) for \(2\le n\le5\), covering \(37{,}440\) edge subsets, reconstructs the exact reliability coefficients, and compares each coefficient with the three-term formula. It also checks degrees, first and second derivatives at \(q=1\), positivity at exact rational arguments for \(2\le n\le20\), and the even-parity \(K_{2,n}\) boundary. Observed result:

`VERIFY_OK independent_connected_graphs=4 edge_subsets=37440 exact_n=2..20`

These computations validate examples and the implementation; the inequalities and derivative calculation above, not finite numerical testing, prove the theorem for all \(n\).

## Relationship to prior work

Brown and McMullin (2026), *On the Real Reliability Roots of Graphs*, ask which graphs have no real zeros, or just one, after removing the unavoidable spanning-tree factor. Their general results establish almost-sure existence of nonreal zeros and a real-root density interval, not this family-wise zero-real-root classification. The present theorem supplies a concrete infinite-family answer to that question.

Brown, Koç and Kooij (2014), *Inflection points for network reliability*, previously state the closed expression for \(R_n\) (in the variable \(p=1-q\)); they study inflection points of related reliability functions. Formula discovery is not the contribution here. Brown and Mol (2017), *On the roots of all-terminal reliability polynomials*, establish root-modulus results but not this exact real-zero count. The earlier general root-location theorem of Brown and Colbourn (1992) allows real nontrivial zeros but does not assert their absence here.

This absence is not universal even for nearby complete bipartite families. Indeed,

\[
R_{K_{2,n}}(q)=(1-q)^n\big((1+q)^n-(2q)^n\big),
\]

and whenever \(n\) is even, it has an additional real root at \(q=-\tfrac13\). Thus a simple general claim for all nonstar complete bipartite graphs would be false.

## Limitations

The theorem concerns only \(K_{3,n}\) with \(n\ge2\), not every \(K_{m,n}\) or arbitrary graph, and provides neither locations nor distinctness of the nonreal zeros. Earlier literature already gives the exact polynomial. A highly relevant 2014 paper was examined through its indexed formula and theorem excerpt; the entire source PDF was not accessible here, so an unobserved discussion there or in unindexed literature remains a bibliographic risk. No independent external validation is claimed.

## References

1. J. I. Brown and I. McMullin, *On the Real Reliability Roots of Graphs*, arXiv:2603.09059v1 (first public version, 2026-03-10), especially Sections 2 and 4. https://arxiv.org/abs/2603.09059
2. J. I. Brown, Y. Koç and R. E. Kooij, *Inflection points for network reliability*, Telecommunication Systems **56** (2014), 79–84. https://doi.org/10.1007/s11235-013-9820-0
3. J. I. Brown and L. Mol, *On the roots of all-terminal reliability polynomials*, Discrete Mathematics **340** (2017), 1287–1299; arXiv:1703.10566. https://arxiv.org/abs/1703.10566
4. J. I. Brown and C. J. Colbourn, *Roots of the reliability polynomial*, SIAM Journal on Discrete Mathematics **5** (1992), 571–585. https://doi.org/10.1137/0405047
5. Oxford-hosted combinatorial thesis (2012), Section 2.6: flow-polynomial real zeros of \(K_{3,n}\), a different Tutte specialization from the reliability polynomial. https://ora.ox.ac.uk/objects/uuid:52070098-14fa-4cf1-ae6e-9f9ce6a626d8
