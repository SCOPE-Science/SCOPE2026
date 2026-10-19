# Exact capacity and period-twelve law for cyclic binary trigram profiles

## Finding

Let \(n\ge1\) and let \(w=w_0w_1\cdots w_{n-1}\in\{0,1\}^n\). Indices are interpreted modulo \(n\), including when \(n<3\). Its **cyclic trigram profile** is the labeled vector
\[
T(w)=(t_{000},t_{001},\ldots,t_{111}),\qquad
 t_{abc}=\#\{i\in\{0,\ldots,n-1\}:(w_i,w_{i+1},w_{i+2})=(a,b,c)\}.
\]
Let \(K(n)=|\{T(w):w\in\{0,1\}^n\}|\) denote the number of attainable profiles. Then
\[
\boxed{\sum_{n\ge1}K(n)z^n=
\frac{z(2-3z+z^2-z^3+5z^5-5z^6+6z^7-7z^8+3z^9)}
{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.}
\]
In particular, \(K(n)\) begins with
\[
2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271,338,419,\ldots
\]
and is an exact degree-four quasipolynomial of **least period twelve**. Its leading term is
\[
\boxed{K(n)=\frac{n^4}{288}+O(n^3).}
\]
The exact maximal cardinality of a length-\(n\) binary code whose distinct codewords have distinct *cyclic trigram count vectors* equals \(K(n)\): choose one representative of each attainable profile.

The proof also gives a complete necessary-and-sufficient feasibility test for every nonnegative integer eight-vector, including all disconnected-support exceptions.

## Assumptions and scope

All words are labeled binary words. The trigram vector records ordered length-three factors **with multiplicity**, including factors that cross the cyclic boundary. The profile does not retain positions or a starting point. The assertion holds for every integer \(n\ge1\), without assuming an aperiodic or primitive source word. The period twelve is the least quasipolynomial coefficient period, not the period of a particular binary word.

For any candidate vector, write
\[
(u,a,c,b,a',d,b',v)
=(t_{000},t_{001},t_{010},t_{011},t_{100},t_{101},t_{110},t_{111}).
\]
Eulerian flow conservation is equivalent to
\[
a=a',\qquad b=b',\qquad a+d=b+c,
\]
where all coordinates are nonnegative integers and the total is \(n\). Thus put \(d=b+c-a\) and require \(c\ge\max(0,a-b)\).

**Exact feasibility classification.** For a nonzero balanced vector, it is attainable if and only if precisely one of the following disjoint possibilities holds:

1. \(a>0,b>0\), with arbitrary \(u,v\ge0\) and permitted \(c\).
2. \(a>0,b=0\), with \(c\ge a\), arbitrary \(u\ge0\), and \(v=0\).
3. \(a=0,b>0\), with arbitrary \(c,v\ge0\), and \(u=0\).
4. \(a=b=0,c=d>0\), with \(u=v=0\).
5. \(a=b=c=d=0\), with exactly one of \(u,v\) strictly positive.

The classification includes both constant cycles and all alternating cycles. No balanced vector outside these cases is realizable by a single cyclic word.

## Proof

**1. Cyclic words and Euler circuits.** Associate to each binary trigram \(ijk\) an arc from vertex \(ij\) to vertex \(jk\) in the four-vertex directed binary de Bruijn graph. A cyclic length-\(n\) word induces a closed walk traversing arc \(ijk\) exactly \(t_{ijk}\) times. Conversely, a directed Euler circuit through a multigraph with these arc multiplicities spells a cyclic word with precisely that profile: write the initial two-symbol vertex, then read the last symbol of each traversed arc. The cyclic overlap is automatic. This works for loops and cycles of length one or two as well.

A nonzero finite directed multigraph has an Euler circuit using all its arcs exactly when every vertex has equal in-degree and out-degree and all non-isolated vertices belong to one connected component of its underlying graph (equivalently here, one strongly connected component). Balance at vertices \(00\), \(11\), and \(01\) gives exactly \(a=a'\), \(b=b'\), and \(a+d=b+c\); the fourth equation is redundant.

**2. Connectivity is completely explicit.** The relevant nonloop arcs are
\[
00\xrightarrow{a}01,\quad 01\xrightarrow{c}10,\quad
01\xrightarrow{b}11,\quad 10\xrightarrow{a}00,\quad
10\xrightarrow{d}01,\quad 11\xrightarrow{b}10,
\]
with loops of multiplicity \(u\) at \(00\) and \(v\) at \(11\).

When \(a,b>0\), the positive arcs already contain the directed four-cycle \(00\to01\to11\to10\to00\); additional arcs or loops cannot disconnect it. If \(a>0,b=0\), conservation implies \(c\ge a>0\), giving \(00\to01\to10\to00\); a loop at \(11\) would be a separate component, so exactly \(v=0\) is necessary. Symmetrically, if \(a=0,b>0\), then \(d=b+c>0\), giving \(01\to11\to10\to01\); exactly \(u=0\) is necessary. If \(a=b=0,c>0\), balance forces \(d=c\) and only \(01\leftrightarrow10\) can be present. If \(a=b=c=0\), all nonloop arcs vanish and a single Euler circuit can use only one of the two loop vertices. These alternatives prove the feasibility classification in both directions.

**3. Enumerate disjoint supports.** Introduce \(z\), which marks the total number of cyclic trigram occurrences, equal to word length. Since \(d=b+c-a\), the total for any balanced vector is
\[
n=u+v+2a+2b+c+d=u+v+a+3b+2c.
\]
The two pure loops contribute \(E(z)=2z/(1-z)\). The alternating profiles contribute \(D(z)=z^2/(1-z^2)\). The two three-vertex support types have identical generating functions and together contribute
\[
B(z)=2\sum_{a\ge1,s,u\ge0}z^{3a+2s+u}=
\frac{2z^3}{(1-z^3)(1-z^2)(1-z)}.
\]
Here \(s=c-a\) in the \(b=0\) case, and \(s=c\) in the \(a=0\) case.

For the four-vertex type \(a,b>0\), sum over \(c\ge\max(0,a-b)\) and \(u,v\ge0\):
\[
A(z)=\frac{1}{(1-z)^2(1-z^2)}
\sum_{a,b\ge1}z^{a+3b+2\max(0,a-b)}.
\]
Split \(1\le a\le b\) from \(a=b+t\), \(t\ge1\). The first contribution to the double sum is
\[
\sum_{b\ge1}\sum_{a=1}^{b}z^{a+3b}
=\frac{z}{1-z}\left(\frac{z^3}{1-z^3}-\frac{z^4}{1-z^4}\right),
\]
and the second is
\[
\sum_{b,t\ge1}z^{4b+3t}=
\frac{z^7}{(1-z^4)(1-z^3)}.
\]
Consequently,
\[
A(z)=\frac{z^4(1-z+z^2)}{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.
\]
Adding \(A+B+D+E\) and simplifying gives the rational function asserted above. The supports are disjoint, so no profile is counted twice.

**4. Degree, least period, and leading coefficient.** The reduced rational denominator has a pole of order five at \(z=1\), simple poles at \(z=-1\), at the primitive fourth roots, and at the primitive third roots. Its numerator, after factoring out \(z\), has nonzero remainders \(-19\), \(-1\), and \(4z\) upon division by \(1+z\), \(1+z^2\), and \(1+z+z^2\), respectively; hence none of these cyclotomic factors cancels. By partial fractions, \(K(n)\) is a degree-four quasipolynomial with period dividing \(\operatorname{lcm}(2,3,4)=12\). The genuine poles at primitive third and fourth roots force every quasipolynomial period to be divisible by both three and four. The least period is therefore twelve. Also,
\[
\lim_{z\to1}(1-z)^5\sum_{n\ge1}K(n)z^n=\frac1{12},
\]
so the leading coefficient of \(K(n)\) is \((1/12)/4!=1/288\).

**5. Coding consequence.** Two source words are observationally confusable precisely when their vectors coincide. Any zero-error code contains at most one word per realized vector, and selecting one word from each nonempty profile class attains this bound. Thus its optimal size is exactly \(K(n)\).

## Verification

The accompanying self-contained `verify.py` is a finite, independent consistency checker. It (i) computes all distinct circular trigram count vectors from all \(2^n\) binary words for every \(1\le n\le18\); (ii) enumerates every nonnegative eight-vector of total \(n\le11\) and compares both the explicit structural criteria and a separately implemented graph Euler-circuit feasibility test against the actual word profiles; and (iii) compares a direct parameter sum with the rational generating function for \(1\le n\le60\). The polynomial coefficients are recovered by an integer recurrence, without symbolic-algebra dependencies. Every test passed when the packaged program was executed.

These checks are finite safeguards; the all-length claims, period, and asymptotic term follow from the proof above, not numerical extrapolation. The checker is not an independent mathematical audit.

## Relationship to prior work

The 2010 work of Jacquet, Knessl, and Szpankowski counts first-order cyclic Markov types and provides asymptotic generalities for balanced matrices; its displayed binary worked example concerns **bigram** matrices, not complete cyclic binary trigram profiles. Kiah, Puleo, and Milenkovic (2014/2015) develop profile vectors in de Bruijn graphs and prove general Ehrhart-type quasipolynomial bounds for constrained substring spectra; their treatment makes a period-dividing-twelve prediction plausible here but does not state this exact unconditioned binary cyclic trigram enumerator, connectivity correction, or its least period. Suzuki and Myers (2022) motivate the use of local k-mer count profiles for sequence inference; their read-classification model neither counts cyclic profile classes nor yields this formula.

These established frameworks and general theorems are not claimed as new. The contribution is the **exact realizable support classification**, the closed rational generating function (including disconnected balanced-vector exclusions), its sharp period, and the exact observation-code cardinality for the order-three binary cyclic case. No general result in those inspected texts was found that already explicitly provides this enumerator. Equivalent exact computations elsewhere remain possible and would supersede any novelty claim.

## Limitations

This is a noiseless profile-capacity result, not a construction with decoding complexity or protection against read errors. It does not give the distribution of profile-class sizes, characterize all maximizing codeword selections, or generalize the formula to larger alphabets or longer observed blocks. The proof does not establish uniqueness against unindexed mathematical literature, and no independent audit has been performed. The cycle is oriented, and distinct words related by rotation are allowed; their identical vector is counted just once.

## References

1. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI: 10.46298/dmtcs.2768. Original full text: https://dmtcs.episciences.org/articles/2768/download.
2. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (first submitted 2015-02-02); related earlier public version *Codes for DNA Storage Channels*, arXiv:1410.8837 (first submitted 2014-10-31). Full texts: https://arxiv.org/abs/1502.00517 and https://arxiv.org/abs/1410.8837.
3. Y. Suzuki and G. Myers, *Accurate k-mer Classification Using Read Profiles*, WABI 2022, DOI: 10.4230/LIPIcs.WABI.2022.10, publicly available 2022-08-26. Full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol242-wabi2022/LIPIcs.WABI.2022.10/LIPIcs.WABI.2022.10.pdf.
