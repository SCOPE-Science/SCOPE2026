# Exact cyclic pair-composition capacity for ternary words with runs of length at most two

## Finding
For every integer \(n\ge2\), the number \(C_n\) of distinct unordered adjacent-pair composition profiles of ternary cyclic words with no run of three identical symbols, including across the boundary, is given by
\[
\sum_{n\ge2}C_nz^n=\frac{z^2P(z)}{(1-z)^6(1+z)^3(1+z^2)^2(1+z+z^2)^2},
\]
where
\[
P(z)=3+4z+2z^2-z^3+z^4+z^5+5z^6+4z^7-z^8-z^9-4z^{10}+z^{12}+z^{13}+z^{14}-z^{15}.
\]
Consequently \(C_n\) is a degree-five quasipolynomial of **exact least period \(12\)** and
\[
C_n=\frac{n^5}{2304}+O(n^4).
\]
The exact maximum size of a zero-error code for this observation equals \(C_n\), by taking one representative source per attainable profile.

The structural result holds over any labeled finite alphabet \(\Sigma=\{0,\ldots,q-1\}\), \(q\ge2\): a histogram \((h_{ij})_{i\le j}\) is attained by a cyclic word of length \(n=\sum_{i\le j}h_{ij}\ge2\) avoiding three identical consecutive symbols precisely if the off-diagonal multigraph with edge multiplicity \(h_{ij}\) for \(i<j\) is nonempty and connected after discarding isolated vertices, every off-diagonal degree \(d_i\) is even, and \(0\le h_{ii}\le d_i/2\) for each symbol.

## Assumptions and scope
An **indexed cyclic word** \(w=(w_0,\dots,w_{n-1})\) has indices modulo \(n\); rotations are different sources but yield the same observed histogram. The no-triple condition requires \(w_i,w_{i+1},w_{i+2}\) not all equal for every cyclic position \(i\). This includes wrapping windows even for \(n=2\). The observed vector has six coordinates \(h_{00},h_{01},h_{02},h_{11},h_{12},h_{22}\), each counting cyclic adjacent pairs with **unordered** symbols; it does not retain pair direction, location, or read ordering. Repetitions and multiplicities are retained. Empty words and length-one words are outside the theorem.

## Proof
**1. Complete realizability criterion.** Let \(d_i=\sum_{j\ne i}h_{\min(i,j),\max(i,j)}\). In any admitted cyclic word, split at each change of symbol. Every maximal monochromatic run has length either one or two. Contract each run to its symbol: the resulting circular succession gives a closed walk using each off-diagonal edge type exactly its prescribed number of times. Hence its nonempty off-diagonal multigraph is connected on active vertices, and each \(d_i\) is even. Each run of symbol \(i\) contributes two incident switching edges; there are exactly \(d_i/2\) such runs. Exactly \(h_{ii}\) of them have length two, whence \(0\le h_{ii}\le d_i/2\).

Conversely, a nonempty connected even-degree off-diagonal multigraph has an Eulerian closed circuit. Read its consecutive visited symbols cyclically. Symbol \(i\) appears as exactly \(d_i/2\) visits; choose \(h_{ii}\) of those visits and double that symbol, leaving all other visits singleton. Consecutive runs have different symbols, including at the circular boundary, so no triple-equal window occurs. Its off-diagonal counts are precisely the multigraph edge multiplicities, and its diagonal counts are the numbers of doubled visits. This proves sufficiency constructively for every \(q\ge2\).

**2. Exact ternary parameterization.** Put \(x=h_{01}\), \(y=h_{02}\), \(t=h_{12}\). The three off-diagonal degrees are \(x+y\), \(x+t\), and \(y+t\). They are all even if and only if the three nonnegative counts have one common parity \(\epsilon\in\{0,1\}\). Therefore, uniquely,
\[
x=2u+\epsilon,\qquad y=2v+\epsilon,\qquad t=2w+\epsilon\qquad (u,v,w\ge0).
\]
For a graph with at most three vertices, any nonempty subset of the three possible undirected edge types forms a connected graph on its nonisolated vertices. Thus connectivity is automatic except when all three counts vanish, the unique excluded parameter \((u,v,w,\epsilon)=(0,0,0,0)\). Denote loops by \(a=h_{00}\), \(b=h_{11}\), \(c=h_{22}\). The necessary and sufficient bounds are
\[
0\le a\le u+v+\epsilon,\qquad 0\le b\le u+w+\epsilon,\qquad 0\le c\le v+w+\epsilon.
\]
The cyclic length is
\[
n=2(u+v+w)+3\epsilon+a+b+c.
\]
Different parameter tuples give different histograms. This yields a direct all-length counting formula:
\[
C_n=\sum_{\epsilon=0}^1\ \sum_{u,v,w\ge0}\ \sum_{a=0}^{u+v+\epsilon}\ \sum_{b=0}^{u+w+\epsilon}\ \sum_{c=0}^{v+w+\epsilon}
[\,2(u+v+w)+3\epsilon+a+b+c=n\,]
- [\,n=0\,],
\]
where the bracket denotes a \(0\)-or-\(1\) indicator.

**3. Rational generating function.** Sum the three finite geometric series for \(a,b,c\). Writing
\[
A_0(z)=\frac1{(1-z^2)^3},\quad
A_1(z)=\frac1{(1-z^2)(1-z^3)^2},\quad
A_2(z)=\frac1{(1-z^3)^2(1-z^4)},\quad
A_3(z)=\frac1{(1-z^4)^3},
\]
we obtain the independently useful expression
\[
F(z)=\frac{(1+z^3)A_0(z)-3(z+z^5)A_1(z)+3(z^2+z^7)A_2(z)-(z^3+z^9)A_3(z)}{(1-z)^3}-1.
\]
Indeed, the expansion of \(\prod_i(1-z^{\text{maximum loop count}_i+1})\) is grouped by the number \(k\) of selected symbols. Of the three undirected off-diagonal edge types, \(\binom{k}{2}\) meet two selected symbols, \(k(3-k)\) meet one, and \(\binom{3-k}{2}\) meet zero. Their independent nonnegative parameters contribute geometric denominators with exponents four, three, and two respectively, giving exactly \(A_k\). The factor \(z^{3\epsilon}\) accounts for parity, while each selected maximum contributes \(z^{(\epsilon+1)k}\). Finally, \(-1\) discards the unique empty graph with zero length.

Elementary common-denominator simplification gives the stated \(z^2P(z)\) rational function. Its denominator is already reduced: the remainders of \(P(z)\) modulo \(z+1\), \(z^2+1\), and \(z^2+z+1\) are respectively \(1\), \(3z\), and \(3z+3\), all nonzero; also \(P(1)=15\ne0\). Its poles are roots of unity of orders dividing \(12\), so coefficients are a quasipolynomial of period dividing \(12\) and degree five. Genuine primitive fourth- and third-root poles force its least period to be divisible by both \(4\) and \(3\), hence exactly \(12\). The coefficient of \((1-z)^{-6}\) at \(z=1\) is \(5/96\); dividing by \(5!\) gives leading coefficient \(1/2304\). There are no positive-length constant-symbol cyclic words satisfying the no-triple condition.

## Verification
Execute the included standalone Python 3 standard-library script as `python3 verify.py`. It independently enumerates every ternary word through length ten, obtains all profiles by an alternative dynamic program through length eighteen, checks the graph criterion against direct word enumeration for alphabets of sizes two through five, compares direct parameter enumeration with the rational recurrence through length forty-five, and constructs and validates 2,000 random Euler-tour witnesses for alphabet sizes three, four, five, and seven. Finite tests are checks, **not** substitutes for the all-length mathematical argument above.

For \(n=2,3,\ldots,18\) the counts are respectively
\[
3,7,12,21,41,63,99,149,219,309,432,582,783,1029,1332,1701,2161.
\]

## Relationship to prior work
Ye and Elishco study reconstruction from length-limited unordered composition multisets for **linear** strings; their setting supplies the motivation but not this cyclic, run-constrained all-length capacity. Kiah, Puleo, and Milenkovic develop general sequence-profile coding and graph-flow machinery for directed substring-frequency observations; the graph viewpoint is relevant background but neither the cyclic unordered-pair realizability criterion with the run ceiling nor the displayed specialized rational enumeration is stated in the material inspected. Nguyen, Cai, Immink, and Kiah study DNA sequence constraints and code design, and İrimağzı, Uslan, and Hareedy analyze run-length-constrained DNA codes, rather than this unordered-pair read-profile cardinality. The overlap argument is by **objects, observation model, constraints, and theorem implication**, not by title alone.

## Limitations
The explicit generating function is proved for the ternary alphabet, not for arbitrary \(q\); the general-alphabet part is the necessary-and-sufficient realizability criterion. The zero-error capacity assumes complete noiseless observations with exact multiplicities, not missing, corrupted, or probabilistically sampled reads. A potentially unindexed equivalent special case in integer-flow enumeration or composition-read literature cannot be eliminated by unsuccessful keyword searches. The finite verifier is not an all-order proof.

## References
- Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, first public 2022-08-31. https://arxiv.org/abs/2208.14963
- H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517. https://arxiv.org/abs/1502.00517
- T. T. Nguyen, K. Cai, K. A. S. Immink, and H. M. Kiah, *Capacity-Approaching Constrained Codes with Error Correction for DNA-Based Data Storage*, arXiv:2001.02839. https://arxiv.org/abs/2001.02839
- C. İrimağzı, Y. Uslan, and A. Hareedy, *Protecting the Future of Information: LOCO Coding With Error Detection for DNA Data Storage*, arXiv:2311.08325. https://arxiv.org/abs/2311.08325
