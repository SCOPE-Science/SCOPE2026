# A vertex-boundary census for minimal Roman functions on one-leaf coronas and a Pell–Lucas law for sunlets

## Finding

For a finite simple graph \(H=(V,E)\) with \(n=|V|\), construct its one-leaf corona \(H\circ K_1\) by adjoining a distinct pendant vertex \(v'\) to each \(v\in V\). An assignment \(f:V(H\circ K_1)\to\{0,1,2\}\) is a Roman dominating function (RDF) if each vertex assigned \(0\) has an adjacent vertex assigned \(2\). An RDF is **pointwise minimal** if no strictly smaller assignment in the coordinatewise order is an RDF. Write \(M_H(z)\) for the polynomial whose coefficient at \(z^j\) is the number of such minimal assignments with total weight \(j\).

For \(S\subseteq V\), write \(\partial_H(S)=N_H(S)\setminus S\), the external vertex boundary, and \(U_H(S)=V\setminus(S\cup\partial_H(S))\). The complete weight census is

\[
\boxed{M_H(z)=\sum_{S\subseteq V}2^{|U_H(S)|}z^{2n-|\partial_H(S)|}.}
\tag{1}
\]

For the sunlet \(S_n=C_n\circ K_1\), \(n\ge3\), write \(M_n(z)=M_{C_n}(z)\). Define the formal auxiliary polynomials \(\widetilde M_1(z)=3z^2\), \(\widetilde M_2(z)=2z^3+5z^4\), and \(\widetilde M_n(z)=M_n(z)\) for \(n\ge3\). These first two polynomials are formal extension coefficients, not claims about nonexistent simple cycles of lengths one or two. Then

\[
\boxed{\sum_{n\ge1}\widetilde M_n(z)t^n
=\frac{z^2t\bigl(3+(2z-4z^2)t+(3z^2-6z^3)t^2\bigr)}
 {1-3z^2t+(2z^4-z^3)t^2+(2z^5-z^4)t^3}.}
\tag{2}
\]

Equivalently, for all \(n\ge4\) with the specified formal initial coefficients,

\[
\widetilde M_n(z)=3z^2\widetilde M_{n-1}(z)
 +(z^3-2z^4)\widetilde M_{n-2}(z)
 +(z^4-2z^5)\widetilde M_{n-3}(z).
\tag{3}
\]

For all integers \(n\ge3\), the total number of pointwise-minimal Roman functions and the number of *minimum-weight* ones are respectively

\[
\boxed{M_n(1)=1+(1+\sqrt2)^n+(1-\sqrt2)^n,}
\tag{4}
\]

\[
\boxed{[z^{\lceil4n/3\rceil}]M_n(z)=
\begin{cases}
3,&n\equiv0\pmod3,\\
 n(n+17)/6,&n\equiv1\pmod3,\\
 n,&n\equiv2\pmod3.
\end{cases}}
\tag{5}
\]

The minimum Roman weight itself is \(\lceil4n/3\rceil\); that scalar equality is included to interpret (5), not asserted as independently new. The census determines every coefficient, not only the minimum.

## Assumptions and scope

All graphs are finite, simple, and labeled. The general identity (1) permits disconnected or empty \(H\), with the empty graph contributing the unique empty function. In the cyclic specializations, \(C_n\) is the simple labeled cycle with \(n\ge3\), and each pendant is distinct. Function weights are sums of all vertex labels. A minimal RDF is minimal in the pointwise function order, **not** merely one achieving minimum possible weight. The labels \(0,1,2\) have their usual Roman-domination meanings.

## Proof

**Step 1: Local minimality test.** An RDF is pointwise minimal if and only if (i) no vertex assigned \(1\) is adjacent to a vertex assigned \(2\), and (ii) every vertex assigned \(2\) has an adjacent zero-valued vertex for which it is the *unique* two-valued neighbor. Necessity follows by lowering a violating \(1\) to \(0\), or lowering a violating \(2\) to \(1\). Conversely, every possible one-coordinate lowering either leaves a newly unprotected zero or removes the unique defender of an existing zero. A strictly lower RDF would imply that a one-coordinate lowering was feasible, by monotonicity of the RDF property under coordinate increases.

**Step 2: Exact corona configurations.** For the core–pendant pair \((v,v')\), the only permissible local assignments are

\[
 A=(2,0),\qquad B=(1,1),\qquad C=(0,1),\qquad D=(0,2).
\]

Indeed a pendant labeled zero needs its own core labeled two; a pendant labeled one cannot neighbor a two by Step 1(i); and a pendant labeled two needs the core as its private zero neighbor, ruling out another core two adjacent to that core. Fix \(S\), the set of core vertices assigned two. For \(v\in S\), the pair must be \(A\), with the zero pendant supplying its private witness. For \(v\in\partial_H(S)\), it must be \(C\): a core zero is defended by a core two, and a two-valued pendant there would lose the uniqueness of its zero witness. For \(v\in U_H(S)\), either \(B\) or \(D\) is allowed. Conversely every such assignment meets both the Roman and minimality conditions in Step 1. This is a bijection, with \(2^{|U_H(S)|}\) choices and weight \(2n-|\partial_H(S)|\), proving (1).

**Step 3: Exact cyclic gap enumerator.** For \(S\ne\varnothing\) on \(C_n\), list the \(k=|S|\) chosen core vertices cyclically and let \(\ell_1,\ldots,\ell_k\ge0\) count the unchosen vertices in the gaps, so \(\sum_i\ell_i=n-k\). A gap of length zero contributes factor \(1\); of length one contributes \(zt\); and of length \(\ell\ge2\) contributes \(z^{2\ell-2}2^{\ell-2}t^\ell\). Thus the gap series is

\[
 H(t,z)=1+zt+\frac{z^2t^2}{1-2z^2t}.
\]

Every cyclic word with \(k\) marked core-two positions has exactly \(k\) possible starting marks among \(n\) labeled positions. Therefore its generating polynomial is

\[
 M_n(z)=(2z^2)^n+\sum_{k=1}^n\frac nk z^{2k}[t^{n-k}]H(t,z)^k,\qquad n\ge3.
\tag{6}
\]

The first term is the no-core-two case: each pair independently chooses \(B\) or \(D\). The same formal coefficient construction also defines \(\widetilde M_1,\widetilde M_2\). Summing (6) formally over all \(n\ge1\), including the two auxiliary orders, gives

\[
 \sum_{n\ge1}\widetilde M_n(z)t^n
 =\frac{2z^2t}{1-2z^2t}
 +t\frac{\partial}{\partial t}\left[-\log\bigl(1-z^2tH(t,z)\bigr)\right].
\]

Rational simplification gives (2), and equating coefficients gives (3). At \(z=1\), the expression becomes \(t/(1-t)+2t(1+t)/(1-2t-t^2)\), whose coefficients establish (4) by the recurrence with characteristic roots \(1\pm\sqrt2\).

**Step 4: Exact minimum multiplicities.** In the gap model, the boundary consists of \(\min\{\ell_i,2\}\) vertices in each gap, hence

\[
 |\partial_{C_n}(S)|=\sum_i\min\{\ell_i,2\}
 \le\min\{n-k,2k\}\le\lfloor2n/3\rfloor.
\]

The bound is attained by gaps of lengths two, except for the short adjustments below. If \(n=3q\), equality requires \(k=q\) and every gap length two, giving exactly three labeled patterns. If \(n=3q+2\), equality requires \(k=q+1\), exactly one gap of length one and all remaining gaps of length two, giving \(n\) patterns. If \(n=3q+1\), there are two possibilities. With \(k=q\), one gap has length three and all others length two; the unique interior vertex of the three-gap has two choices \(B,D\), giving \(2n\) functions. With \(k=q+1\), all gaps have length at most two; either one gap has length zero (\(n\) patterns) or two gaps have length one (\(nq/2\) patterns). The total in this case is \(2n+n+nq/2=n(n+17)/6\). Since all minimum-weight functions are among these and all are feasible, their number is (5), and their common weight is \(2n-\lfloor2n/3\rfloor=\lceil4n/3\rceil\).

## Verification

The standalone file `verify.py` independently checks Roman domination and pointwise minimality by all one-coordinate decreases on directly constructed graphs, without invoking the structural characterization. For every labeled base graph on at most four vertices (75 graphs; 425,907 assignments), it compares the brute-force weight distribution to (1). For all sunlets of orders three through six it checks 597,780 ternary assignments; for cyclic words of orders three through nine it checks 349,504 four-state assignments. It also checks the recurrence, integer Pell–Lucas totals, minimum degrees, and formula (5) through order 24. The actual stdout is stored as `verification_output.txt`. These finite tests support, but do not replace, the unrestricted proof.

For reproduction with Python 3 and no external packages, run `python3 verify.py` in a directory containing the standalone file.

Examples include \(M_3(z)=3z^4+3z^5+9z^6\), \(M_4(z)=14z^6+4z^7+17z^8\), and \(M_5(z)=5z^7+40z^8+5z^9+33z^{10}\).

## Relationship to prior work

Abu-Khzam, Fernau and Mann developed the theory and enumeration algorithms for pointwise-minimal Roman functions, including a general uniqueness theorem for a fixed set of vertices carrying label two. Their work already supplies general-purpose structural tests; it is not a new part of the present claim. Their graph-class census includes paths, forests, interval and related classes, but the inspected texts do not state the exact corona-boundary polynomial (1), the sunlet generating function (2), or the cyclic minimum-multiplicity formula (5).

Earlier papers by Siva Parvathi and Maheswari exhibit particular minimal Roman functions on corona products involving a cycle with complete graphs or a path with a star. Those constructions are a relevant predecessor, not complete counts of pointwise-minimal functions on one-leaf coronas. General Roman-domination-number and vertex-differential identities may imply scalar optima; no novelty is claimed for a scalar optimum alone.

## Limitations

The sunlet formulas do not assert analogous closed rational functions for arbitrary corona attachments or arbitrary base graphs. General (1) is a finite exact subset sum and does not establish polynomial-time coefficient computation for arbitrary input \(H\). The auxiliary coefficients at orders one and two are formal enumerative devices, not instances of simple cycles. Bibliographic priority relative to inaccessible or unindexed literature remains uncertain. Independent validation has not been performed.

## References

1. F. N. Abu-Khzam, H. Fernau and K. Mann, *Minimal Roman Dominating Functions: Extensions and Enumeration*, arXiv:2204.04765, first public version 10 April 2022; expanded open-access journal article in *Algorithmica* 86 (2024), DOI:10.1007/s00453-024-01211-w.
2. F. N. Abu-Khzam, H. Fernau and K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261, first public version 10 August 2022; MFCS 2023.
3. M. Siva Parvathi and B. Maheswari, *Some Variations of Y Dominating Functions of Corona Product Graph of a Cycle with a Complete Graph*, *International Journal of Computer Applications* 81(1), 2013, DOI:10.5120/13975-1966, section 5.
4. M. Siva Parvathi and B. Maheswari, *Roman Dominating and Total Dominating Functions of Corona Product Graph of a Path with a Star*, *International Journal of Computer Engineering and Technology* 5(1), 2014, pp. 21–27.
