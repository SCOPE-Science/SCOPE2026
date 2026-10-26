# Exact cyclic binary three-gram profile enumeration

## Finding

For every integer \(n\ge1\), let \(C_n\) be the number of different **multiplicity vectors of cyclic contiguous three-bit factors** attainable by words \(w\in\{0,1\}^n\). Each starting position contributes one factor, with all subscripts interpreted modulo \(n\), including when \(n=1\) or \(2\). Thus each profile is an eight-coordinate nonnegative integer vector whose entries sum to \(n\). Circular rotation does not change the profile.

The exact ordinary generating function is

\[
\begin{aligned}
F(z)=\sum_{n\ge1}C_n z^n={}&
\frac{z^4(1+z^3)}{(1-z^4)(1-z^3)(1-z^2)(1-z)^2}\\
&+\frac{2z^3}{(1-z^3)(1-z^2)(1-z)}
+\frac{z^2}{1-z^2}+\frac{2z}{1-z}.
\end{aligned}
\]

The first eighteen exact values, indexed by \(n=1,\ldots,18\), are

\[
(C_1,\ldots,C_{18})=(2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271,338,419).
\]

Consequently \(C_n\) is a quasipolynomial in \(n\) with period dividing \(12\), and

\[
C_n=\frac{n^4}{288}+O(n^3).
\]

The coefficient \(1/288\) was already established in earlier work on Markov-type / sequence-profile enumeration; **it is not claimed as new here**. The result is the explicit all-length rational generating function and its complete boundary-connectivity corrections. Equivalently, \(C_n\) is the largest possible number of length-\(n\) binary necklaces in a code with mutually distinct cyclic three-gram multispectra.

## Assumptions and scope

A binary cyclic word is a nonempty length-\(n\) word with indices in \(\mathbb Z/n\mathbb Z\). A cyclic three-gram starting at position \(i\) is \((w_i,w_{i+1},w_{i+2})\). Let \(x_{uvw}\) be the count of cyclic three-grams \(uvw\in\{0,1\}^3\); the profile is the ordered tuple of the eight counts, in lexicographic order. Rotations are identified for the code interpretation, but two different necklaces may share a profile. Complementation and reversal are *not* used to identify profiles. Repeated visits and edge multiplicities are allowed.

No probabilistic assumptions are needed. The result holds for every positive integer \(n\). The generating function is a formal power series at \(z=0\).

## Proof

**Flow representation.** Use the binary order-two de Bruijn directed graph, with vertices \(00,01,10,11\) and an edge labeled \(uvw\) from \(uv\) to \(vw\). A cyclic word determines a closed directed walk whose multiplicities on labeled edges are its cyclic three-gram counts. Conversely, a nonzero integral edge-multiplicity vector comes from a cyclic word exactly when in-degree equals out-degree at every vertex and the undirected support on vertices of positive degree is connected. Indeed, such a balanced connected directed multigraph has a directed Eulerian circuit. Reading consecutive overlaps around the circuit gives a cyclic word, including loops and short cycles.

**Balance parametrization.** Write

\[
\begin{gathered}
a=x_{000},\quad h=x_{111},\quad
p=x_{001}=x_{100},\quad q=x_{011}=x_{110},\\
r=x_{010},\qquad s=x_{101}=r+q-p.
\end{gathered}
\]

The equalities follow from degree balance at \(00\), \(11\), and \(01\), respectively. Conversely, these equalities imply degree balance at all vertices. Thus \(a,h,p,q,r\) range over nonnegative integers subject to \(s=r+q-p\ge0\) and

\[
n=a+h+p+3q+2r.
\]

Each parameter quintuple determines a unique profile. We now impose connectedness. The possibilities below are **disjoint and exhaustive**.

**Case I: \(p,q\ge1\).** The positive edge cycles \(00\to01\to11\to10\to00\) connect all four vertices, regardless of any other counts. When \(q\ge p\), write \(q=p+t\) and \(r=k\), with \(p\ge1\), \(t,k\ge0\), obtaining \(n=4p+3t+2k+a+h\). When \(p>q\), write \(p=q+t\), \(r=t+k\), with \(q,t\ge1\), \(k\ge0\), again obtaining \(n=4q+3t+2k+a+h\). Counting nonnegative slack variables gives

\[
\frac{z^4(1+z^3)}{(1-z^4)(1-z^3)(1-z^2)(1-z)^2}.
\]

**Case II: \(p\ge1,q=0\).** Since \(s=r-p\ge0\), put \(r=p+k\), \(k\ge0\). The support containing \(00,01,10\) is connected, while \(11\) is isolated and must have no positive loop; thus \(h=0\). We have \(n=3p+2k+a\), contributing

\[
\frac{z^3}{(1-z^3)(1-z^2)(1-z)}.
\]

**Case III: \(p=0,q\ge1\).** Here \(s=r+q>0\), and the connected nontrivial support contains \(01,10,11\). The loop at \(00\) must be absent, so \(a=0\). Thus \(n=3q+2r+h\), contributing the same series as Case II.

**Case IV: \(p=q=0,r\ge1\).** Then \(s=r\) and \(01\leftrightarrow10\) is a connected component. Both constant loops must be absent, \(a=h=0\). Thus \(n=2r\), contributing \(z^2/(1-z^2)\).

**Case V: \(p=q=r=0\).** Only the two constant loops remain. They cannot both be positive in a single circuit, so exactly one of \(a,h\) is positive, contributing \(2z/(1-z)\).

Summing the five disjoint series gives the displayed rational generating function, proving the exact count for every \(n\ge1\). Its denominator divides a product of powers of \((1-z^k)\) with \(k=1,2,3,4\), so partial fractions show quasipolynomial behavior with period dividing \(\operatorname{lcm}(1,2,3,4)=12\). The only pole of order five is at \(z=1\), where the first summand is asymptotic to \(\frac{1}{12}(1-z)^{-5}\); the other summands have lower-order poles. Consequently \(C_n=\frac{1}{12}\binom{n+4}{4}+O(n^3)=n^4/288+O(n^3)\).

Finally, the cyclic profile mapping partitions the finite set of binary necklaces into exactly \(C_n\) nonempty fibers. A zero-error multispectrum code selects at most one representative per fiber, and selecting one from every fiber attains \(C_n\).

## Verification

The included standalone Python file `checker.py` requires only the standard library. Execute `python3 checker.py` in the directory containing this document. It verifies three finite encodings: direct enumeration of cyclic profiles of all \(2^n\) binary words for \(1\le n\le15\); separate enumeration of nonnegative degree-balanced edge counts with an independent undirected support-connectivity test for \(1\le n\le19\); and coefficients from independent finite geometric-series expansions of the five structural cases. The methods agree and recover the eighteen listed coefficients. The infinite statement follows from the above proof, **not** from a finite computation.

## Relationship to prior work

Tesler (2017, arXiv:1708.03654) develops cyclic multi de Bruijn sequences with every \(k\)-mer appearing at a fixed common multiplicity, including explicit enumerations of such sequences. The present problem allows *arbitrary, varying* three-gram multiplicities and counts attainable count vectors, rather than cyclic sequences realizing a fixed vector. That difference makes the five support-connectivity cases necessary.

Kiah, Puleo, and Milenkovic (2015, arXiv:1502.00517) introduce sequence-profile reconstruction using de Bruijn flow constraints and Ehrhart theory, and list the **same leading constant \(1/288\)** for the binary three-gram case (Table I). Their enumerative results give asymptotic and general lattice-polytope information, not this explicit all-length cyclic enumeration with connected-support exceptions. Jacquet, Knessl, and Szpankowski (2010/2012, DOI 10.46298/dmtcs.2768 and 10.1109/TIT.2012.2191476) analyze general Markov-type counting and derive corresponding asymptotic methods, not the present five-case finite generating function. Yehezkeally, Marcovich, and Yaakobi (2021, arXiv:2108.11725) formulate multiset substring reconstruction and asymptotic coding questions for linear, potentially multiple strands, without this cyclic binary three-gram coefficient sequence.

The general Eulerian-circuit criterion and rational generating-function technique are established; no novelty is claimed for either. The specific complete coefficient formula is the new result asserted here.

## Limitations

This is a binary, cyclic, **length-three** result; it does not enumerate arbitrary read lengths, larger alphabets, the number of necklaces per profile, or error-correcting codes robust to corrupted profiles. The quantitative leading asymptotic is previously known. More general published lattice-point machinery may be specialized algorithmically to the same count; a previously unnoticed explicit specialization cannot be excluded. The finite checker supplements, but cannot certify, the all-length proof. No independent external review has been performed.

## References

1. G. Tesler, *Multi de Bruijn Sequences*, arXiv:1708.03654 (first public 2017-08-11); Journal of Combinatorics 8(3), 439–474 (2017).
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (2015), particularly Section 3 and Table I.
3. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, Discrete Mathematics & Theoretical Computer Science, AofA'10, DOI 10.46298/dmtcs.2768 (2010); expanded IEEE Transactions on Information Theory paper DOI 10.1109/TIT.2012.2191476 (2012).
4. Y. Yehezkeally, S. Marcovich, E. Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725 (2021).
