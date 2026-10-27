# Exact quiet-pattern weight enumerators for two generalized Petersen families

## Finding
For every \(k\in\{2,3\}\) and every integer \(n\ge 2k+1\), the complete binary Hamming-weight distribution of the strategies that do **nothing** in ordinary closed-neighborhood Lights Out on the generalized Petersen graph \(GP(n,k)\) is governed by six fixed polynomials, despite the graph having \(2n\) vertices.

Put \(h=\gcd(n,2^{k-1})\), \(\delta=1\) if \(5\mid n\) and \(\delta=0\) otherwise, and \(m=h5^\delta\). With \(W_{n,k}(z)=\sum_{q\in\mathcal Q_{n,k}}z^{\operatorname{wt}(q)}\), the complete result is
\[
W_{n,k}(z)=P_{h,\delta}(z^{n/m}),\qquad \dim_{\mathbb F_2}\mathcal Q_{n,k}=h+4\delta.
\]
The six polynomials are:

| \(h\) | \(\delta\) | \(m\) | \(P_{h,\delta}(z)\) |
|:--:|:--:|:--:|:--|
| 1 | 0 | 1 | \(1+z^2\) |
| 1 | 1 | 5 | \(1+15z^4+15z^6+z^{10}\) |
| 2 | 0 | 2 | \(1+2z^2+z^4\) |
| 2 | 1 | 10 | \(1+15z^8+32z^{10}+15z^{12}+z^{20}\) |
| 4 | 0 | 4 | \(1+14z^4+z^8\) |
| 4 | 1 | 20 | \(1+55z^{16}+144z^{20}+55z^{24}+z^{40}\) |

The minimum positive strategy weight is \(4n/5\) if \(5\mid n\); otherwise it is \(n\) for even \(n\) and \(2n\) for odd \(n\). The number of strategies solving any solvable configuration is \(2^{h+4\delta}\), and the fraction of solvable configurations is \(2^{-(h+4\delta)}\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph \(GP(n,k)\) has outer vertices \(u_i\) and inner vertices \(v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\); its edge set consists precisely of \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\). The restrictions \(k\in\{2,3\}\) and \(n\ge2k+1\) ensure the standard simple cubic graph. A move at a vertex toggles that vertex and all its neighbors. A quiet strategy is a binary vector in \(\ker_{\mathbb F_2}(I+A(GP(n,k)))\); its Hamming weight is the number of pressed vertices, counted across both rings. The result concerns the **single-player, unrestricted** binary game, not a constrained two-player game.

## Proof
Write a press vector as an outer binary sequence \(x=(x_i)\) and inner binary sequence \(y=(y_i)\). Let \(T\) denote the cyclic shift of a length-\(n\) sequence, so \((Tx)_i=x_{i+1}\). The quiet-strategy equations are exactly
\[
(1+T+T^{-1})x+y=0,\qquad x+(1+T^k+T^{-k})y=0
\]
in characteristic two. Hence \(y=(1+T+T^{-1})x\), and the entire kernel is isomorphic to the solutions of \(F_k(T)x=0\), where multiplication by the invertible \(T^{k+1}\) gives
\[
F_k(t)=(t^2+t+1)(t^{2k}+t^k+1)+t^{k+1}.
\]
A direct identity in \(\mathbb F_2[t]\) gives, for \(k=2\) and \(k=3\) respectively,
\[
F_2(t)=(t+1)^2(1+t+t^2+t^3+t^4),\qquad
F_3(t)=(t+1)^4(1+t+t^2+t^3+t^4).
\]
Since \(T^n=1\), the outer-sequence space is the cyclic module \(\mathbb F_2[t]/(t^n+1)\). The dimension of a polynomial's annihilator on this module is the degree of its greatest common divisor with \(t^n+1\). The factor \(1+t+t^2+t^3+t^4\) is irreducible of degree four over \(\mathbb F_2\) and divides \(t^n+1\) precisely when \(5\mid n\). The multiplicity of \(t+1\) in \(t^n+1\) is \(2^{\nu_2(n)}\). Consequently \(\deg\gcd(F_k,t^n+1)=h+4\delta\). This proves the dimension assertion.

The same coprime factors give an explicit description of **every** outer pattern. If \(5\nmid n\), then \(x\) is an arbitrary \(h\)-periodic binary sequence. If \(5\mid n\), the outer pattern is a sum \(x_i=a_{i\bmod h}+b_{i\bmod5}\), where \(a\) is arbitrary subject to \(a_0=0\) and \(b\) is an arbitrary binary five-word. The two periodic subspaces intersect exactly in their constant words, since \(\gcd(h,5)=1\); fixing \(a_0=0\) makes this decomposition unique. Indeed the first summand is annihilated by \((T+1)^h\), the second by the degree-five polynomial \(T^5+1\), and their spans have exactly \(h+4\) dimensions. Thus each quiet strategy \((x,y)\) has period dividing \(m=h5^\delta\), and these descriptions exhaust its \(2^{h+4\delta}\) possibilities.

For each of the six pairs \((h,\delta)\), enumerate the \(2^{h+4\delta}\le256\) uniquely parametrized binary base words of length \(m\) and calculate \(y_i=x_i+x_{i-1}+x_{i+1}\pmod2\). The exact integer sum of \(z^{\sum_{i=0}^{m-1}(x_i+y_i)}\) is the displayed polynomial \(P_{h,\delta}(z)\). The included standalone `verify.py` specifies the exhaustive loops and checks all six tables with integer arithmetic; the required search sizes are respectively \(2,32,4,64,16,256\). Because each base word repeats exactly \(n/m\) times, all weights multiply by \(n/m\); this proves the full all-parameter formula, not merely a finite-range guess.

The nonzero minimum exponents in the six displayed polynomials immediately give the stated distances. Finally, a linear map on \(\mathbb F_2^{2n}\) with kernel dimension \(d=h+4\delta\) has \(2^{2n-d}\) image vectors and exactly \(2^d\) preimages of each image vector. These are precisely the solvability and multiplicity claims.

## Verification
The standalone Python 3 script `verify.py` builds each graph directly as a cubic edge set and independently performs exact binary row elimination on its full \(2n\times2n\) closed-neighborhood matrix. It enumerates every resulting binary kernel codeword and compares its weight histogram with the formula for **all** \(k\in\{2,3\}\) and admissible \(n\le80\) (150 distinct graph cases), including all divisibility regimes. Independently, it multiplies the annihilator polynomials in \(\mathbb F_2[t]\) and exhausts all six periodic base-word enumerators. Exact computation confirms every asserted finite table. The infinite-family proof above rests on the polynomial identity and cyclic-module decomposition, not on the cutoff at 80.

Run with `python3 verify.py`; successful output begins with `VERIFY_OK`.

## Relationship to prior work
Torrence and Torrence, *An iterative strategy for Lights Out on Petersen graphs* (2016), investigate precisely the same closed-neighborhood game on generalized Petersen graphs, prove a general nonsingularity criterion (their Theorem 11), and **tabulate nullities for every available parameter with \(n\le40\)** (their Table 1). Those pre-existing finite nullities are acknowledged, not claimed as discoveries. The present claim gives a uniform dimension formula **for arbitrary \(n\)** and, more importantly, the complete weight enumerator of all quiet strategies, including their minimum weights. The inspected text and tables of that article do not determine the latter distributions. Minevich's 2012 note supplies general symmetric-binary-matrix and graph toggling context, but neither these cyclic graph families nor a weight-enumerator theorem. Fiorini and collaborators (2024) examine generalized Petersen graphs for a **different, move-restricted two-player impartial Toggle game**, computing Nimbers rather than kernels of the unrestricted linear toggling operator. Searches for equivalent and stronger all-parameter weight enumerators did not identify coverage; see the review for qualifications.

## Limitations
Only steps \(k=2,3\) are covered; no formula for arbitrary \(k\) is asserted. The six tiny base enumerations are exhaustive finite calculations embedded in a rigorous arbitrary-size reduction, not a general symbolic formula for arbitrary graph codes. Prior work already determines certain finite nullities, and standard linear algebra already explains the relationship between nullity and solution counts. The independently unresolved issue is exhaustive originality among inaccessible or unindexed literature on quiet-pattern weight enumerators; no claim of external certification is made.

## References
1. B. Torrence and R. Torrence, *An iterative strategy for Lights Out on Petersen graphs*, Involve **9** (2016), 721–731, doi:10.2140/involve.2016.9.721, https://msp.org/involve/2016/9-5/involve-v9-n5-p01-p.pdf. Inspected full text, especially Section "Results for Petersen graphs" and Table 1.
2. I. Minevich, *Symmetric Matrices over F2 and the Lights Out Problem*, arXiv:1206.2973v1, first posted 2012-06-14, https://arxiv.org/pdf/1206.2973. Full text inspected.
3. E. Fiorini, M. Fogler, K. Levandosky, B. Lu, J. Porter, and A. Woldar, *On the Nature and Complexity of an Impartial Two-Player Variant of the Game Lights-Out*, arXiv:2411.08247v1 (2024), https://arxiv.org/pdf/2411.08247. Sections on the game rules, generalized Petersen graphs, and numerical tables inspected.
