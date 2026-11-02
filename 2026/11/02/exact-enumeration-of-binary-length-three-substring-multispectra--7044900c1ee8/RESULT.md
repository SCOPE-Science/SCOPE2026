# Exact enumeration of binary length-three substring multispectra

## Finding
For each integer \(n\ge2\), assign to every binary word \(w\in\{0,1\}^n\) the eight-entry vector \(\operatorname{prof}_3(w)=(|w|_u)_{u\in\{0,1\}^3}\), where \(|w|_u\) counts overlapping, contiguous occurrences of \(u\). Let \(R_n\) be the number of **distinct** such vectors (not the number of words and not the number of vectors meeting only linear balance equations). Then the exact ordinary generating function is

\[
\boxed{\displaystyle
\sum_{n\ge2}R_n z^{n-2}=
\frac{1+5z-6z^2+5z^3-z^4+6z^5+3z^6+z^7-z^8-2z^9+2z^{10}}
{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.}
\]

The initial values \(R_2,R_3,\ldots,R_{14}\) are \(1,8,15,28,52,92,151,240,363,532,757,1048,1416\). For all \(n\), \(R_n\) is a degree-four quasipolynomial in \(n\) of **minimal period 12**, with

\[
R_n=\frac{13}{288}n^4+O(n^3).
\]

The value \(R_n\) is also the maximum cardinality of a length-\(n\) binary code whose words can all be distinguished without error from complete, unordered, multiplicity-preserving length-three reads: one representative per profile attains it, and two words with the same profile cannot both belong to such a code.

## Assumptions and scope
The alphabet is ordered only for indexing; no cyclic wraparound occurs. Reads have **fixed length three**, overlap, and retain full multiplicity but not position. The word length satisfies \(n\ge2\); at \(n=2\) there are zero reads and one (all-zero) profile. Write \(m=n-2\), so the coefficient of \(z^m\) counts profiles with exactly \(m\) read occurrences. All statements concern the full unrestricted binary alphabet and all eight possible reads.

## Proof
**1. Euler-trail characterization.** Associate vertices \(00,01,10,11\) with the binary de Bruijn graph of order two, and identify each three-letter word \(abc\) with the arc \(ab\to bc\). A read profile is precisely the vector of arc multiplicities along a directed walk. A nonnegative arc-multiplicity vector is realizable as a length-\(m\) walk if and only if (a) all vertices incident to positive-count edges belong to one weakly connected component and (b) outdegree minus indegree is either zero at every vertex or equals \(+1\) at one vertex and \(-1\) at one other vertex. These are the standard necessary and sufficient Euler-trail conditions. The empty profile is realized when \(m=0\).

Write the multiplicities in lexicographic order as \((a,b,c,d,e,f,g,h)\), corresponding to \((000,001,010,011,100,101,110,111)\). The two self-loops \(a,h\) lie at \(00,11\), respectively. The six other edges are, in order \(b,c,d,e,f,g\),

\[
00\to01,\quad01\to10,\quad01\to11,\quad10\to00,\quad10\to01,\quad11\to10.
\]

Let \(\Delta\) consist of the zero four-vector and all twelve vectors \(\mathbf e_s-\mathbf e_t\), \(s\ne t\), indexed by the four vertices. Every nonnegative vector has a **unique** imbalance \(\delta\in\Delta\) if it is trail-realizable; the thirteen alternatives therefore are disjoint.

**2. Support inclusion-exclusion.** Let \(E=\{b,c,d,e,f,g\}\). For a subset \(T\subseteq E\), define \(A_\delta(T;z)\) as the generating series of nonnegative multiplicities of just these six edges, supported inside \(T\), with imbalance \(\delta\); each vector contributes \(z^{b+c+d+e+f+g}\). For a nonempty support \(S\subseteq E\) connected as an undirected graph on its incident vertices, put \(v(S)=\mathbf1_{\{00\in V(S)\}}+\mathbf1_{\{11\in V(S)\}}\). Once the exact nonloop support is \(S\), loops may be added freely at its incident loop vertices, and nowhere else, giving the factor \((1-z)^{-v(S)}\).

The vectors having only loops and no other edges contribute \(1+2z/(1-z)\). The unique component requirement and inclusion-exclusion over **exact** nonloop supports now give

\[
H(z)=1+\frac{2z}{1-z}+\sum_{\delta\in\Delta}\sum_{T\subseteq E}C_T(z)A_\delta(T;z),
\qquad
C_T(z)=\sum_{\substack{S\supseteq T,\ S\ne\varnothing,\\S\text{ connected}}}
\frac{(-1)^{|S|-|T|}}{(1-z)^{v(S)}}.
\]

This identity counts each realizable profile once; no division by the number of Euler trails is made. Only eleven of the 64 coefficients \(C_T\) are nonzero. In the following exact table, a row \((r_0,r_1,r_2)\) means \(C_T=r_0+r_1/(1-z)+r_2/(1-z)^2\):

| \(T\) | \((r_0,r_1,r_2)\) |
|---|---|
| \(\varnothing\) | \((-1,0,-2)\) |
| \(\{b\},\{d\},\{e\},\{g\}\) | \((0,0,1)\) each |
| \(\{d,e\},\{b,g\}\) | \((0,0,-1)\) each |
| \(\{c,f\}\) | \((1,-2,1)\) |
| \(\{b,c,e,f\},\{c,d,f,g\}\) | \((0,1,-1)\) each |
| \(E\) | \((0,0,1)\) |

The table is a finite 64-support incidence calculation, not a numerical extrapolation. It may be reproduced simply by iterating all nonempty connected subsets of six edges in the displayed definition of \(C_T\).

**3. Evaluation of the support series.** Set \(\delta=(\delta_{00},\delta_{01},\delta_{10},\delta_{11})\). Flow conservation gives the exact parametrization

\[
e=b-\delta_{00},\qquad g=d+\delta_{11},\qquad
f=c+d-b-\delta_{01},\qquad
b+c+d+e+f+g=b+3d+2c-\delta_{00}-\delta_{01}+\delta_{11}.
\]

All six multiplicities must be nonnegative, and an edge absent from \(T\) is set to zero. The allowed ranges of \(b,d\) are each either a fixed nonnegative integer or a lower-bounded ray; their minimum bounds are at most one (at most two after subtracting a fixed value from a ray). Put \(r=-\delta_{01}\). According as \(c,f\) are both permitted, only \(c\) is permitted, only \(f\) is permitted, or neither is permitted, the remaining \(c\)-sum is respectively (i) \(c\ge\max(0,b-d+\delta_{01})\), (ii) \(c=b-d+\delta_{01}\ge0\), (iii) \(c=0\) with \(b-d+\delta_{01}\le0\), or (iv) \(c=0\) with \(b-d+\delta_{01}=0\). Case (i) introduces a factor \((1-z^2)^{-1}\); all four reduce to two-variable geometric series.

For integers \(B,D\ge0\), \(p,q>0\), \(p+q=4\), define

\[
S_{\ge}(p,q,r;B,D)=\sum_{\substack{b\ge B,\ d\ge D\\b-d\ge r}}z^{pb+qd}.
\]

Writing \(t=b-d\) gives the following **formal rational identity**, where an upper limit below the lower limit denotes an empty sum and \(L=\max(r,B-D)\):

\[
S_{\ge}(p,q,r;B,D)=\frac{\displaystyle\sum_{t=r}^{B-D-1}z^{4B-qt}+
\frac{z^{4D+pL}}{1-z^p}}{1-z^4}.
\]

The corresponding \(S_{\le}\) is \(S_{\ge}(q,p,-r;D,B)\), and equality is the difference of two consecutive \(S_{\ge}\) series. Fixed values of \(b\) or \(d\) are imposed by subtracting their lower-bound rays shifted by one. Consequently each \(A_\delta(T;z)\) is evaluated by finitely many displayed geometric-series operations, without any unspecified counting oracle.

Substituting these evaluations and the eleven rows of the support table into the expression for \(H(z)\), and collecting rational terms, gives

\[
(1-z)^3(1-z^2)(1-z^3)(1-z^4)H(z)
=(1-z^2)P(z),
\]

where

\[
P(z)=1+5z-6z^2+5z^3-z^4+6z^5+3z^6+z^7-z^8-2z^9+2z^{10}.
\]

Here the rational-function collection can also be **certified using only finite integer arithmetic with a proved degree bound**. The geometric-series formulas show that \(D_0(z)H(z)\), for \(D_0=(1-z)^3(1-z^2)(1-z^3)(1-z^4)\), is a polynomial of degree at most \(28\): the bounds \(B,D\le2\), \(-1\le r\le1\) give monomial exponents at most \(14\) before the imbalance shift (of absolute value at most two), and multiplication by \(D_0\), of degree 12, gives at most 28. Therefore checking all coefficients through degree \(28\) of the displayed identity is an **exhaustive symbolic polynomial certificate**, not an extrapolation from a sequence. The supplied checker performs the exact coefficient comparison through degree \(40\) from the independent flow counting formula; it also compares against direct word enumeration. Finally,

\[
D_0=(1-z^2)(1-z)^5(1+z)(1+z^2)(1+z+z^2),
\]

so cancellation of \(1-z^2\) proves the rational generating function in the finding.

**4. Asymptotics and minimal period.** The numerator has \(P(1)=13\), while the nonvanishing denominator factors at one multiply to \(2\cdot2\cdot3=12\). Hence \(H(z)\sim 13/[12(1-z)^5]\) and coefficient extraction yields \(R_n=13n^4/288+O(n^3)\). All poles other than one are roots of unity of orders dividing twelve, yielding a degree-four quasipolynomial of period dividing twelve. Since the remainders of \(P\) modulo \(1+z\), \(1+z^2\), and \(1+z+z^2\) are, respectively, \(-17\), \(3z\), and \(8z+8\), none of these cyclotomic poles cancels. The coefficient sequence therefore genuinely requires periods divisible by 2, 4 and 3, and its minimal quasipolynomial period is twelve.

## Verification
Run \(`python3 checker.py`\) in the folder containing this document. The file uses only Python's standard library. It performs three mathematically different tests: direct construction and hashing of all binary word profiles for lengths 3 through 16, three-parameter Eulerian-profile enumeration through 40 reads, and equality of the two polynomial sides through coefficient 40. The last check, combined with the degree-at-most-28 argument in the proof, certifies the exact rational identity for every length. The program prints three `PASS` messages on success. No finite word enumeration is used as a substitute for the degree bound.

## Relationship to prior work
The definition of a complete read-multiplicity profile and its interpretation as a reconstruction-code equivalence class appear in Kiah, Puleo and Milenkovic (first publicly posted in 2014; expanded in 2015), especially Sections 2–4 and the binary length-three example in their numerical discussion. The paper establishes asymptotic growth through Ehrhart techniques and reports the leading \(1/288\) constant for **closed balanced** binary length-three profiles; it does not give the above exact full **open-trail** length-by-length generating function or the explicit period-twelve law. In particular, closed balanced profile counts must not be confused with open-path counts: the present leading constant is \(13/288\). Jacquet, Knessl and Szpankowski (2010; extended 2012) derive Markov-type asymptotics for the order-one (adjacent-pair) model. That general framework motivates, but does not state, this particular full length-three profile enumerator. General Euler-trail existence and Ehrhart rationality do not alone specify its numerator or exact coefficients.

## Limitations
The result concerns **binary** sequences, **all** length-three reads, **linear** words and an error-free multiplicity-preserving readout. It does not solve error-correcting code design at positive distance, resolve the relative positions of reads, count multiplicities within a profile equivalence class, or give analogous formulas for longer reads or larger alphabets. Priority checks cannot exclude every unpublished source or inaccessible exact formula; independent mathematical audit has not been performed.

## References
- H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837, first publicly posted 2014-10-31, https://arxiv.org/abs/1410.8837 . This precursor already contains the relevant complete-read profile definition, asymptotic enumeration, and length-three binary example; its full open-access text was inspected. The expanded *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (2015), https://arxiv.org/abs/1502.00517 , was also inspected.
- P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), https://doi.org/10.46298/dmtcs.2768 ; open proceedings text: https://dmtcs.episciences.org/articles/2768 . The relevant order-one framework and formulas were inspected.
- P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Trans. Information Theory 58 (2012), 4261–4272, https://doi.org/10.1109/TIT.2012.2191476 . Related stronger asymptotic work; the complete journal version was not independently inspected.
