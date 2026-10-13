# Exact periodic-orbit zeta function for antisquare-good binary words
## Finding
Let \(X\subset\{0,1\}^{\mathbb Z}\) be the two-sided shift consisting of every bi-infinite binary sequence with no factor of the form \(u\overline u\) for a binary word \(u\) of length at least \(2\), where \(\overline u\) denotes the bitwise complement. Equivalently, the only permitted antisquares are \(01\) and \(10\); such sequences are called *good*.

For every integer \(n\ge1\), let
\[
P_n=|\{x\in X:\sigma^n x=x\}|,
\]
where \(\sigma\) is the left shift and points are counted with a marked coordinate (not modulo rotation). The Artin–Mazur zeta function of this shift is the following exact rational function, as a formal power series:
\[
\boxed{\zeta_X(z)=\exp\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right)
=\frac{1}{(1-z-z^4-z^6)^2}.}
\]
In particular, the periodic-point enumerator is
\[
\sum_{n\ge1}P_nz^n
=\frac{2(z+4z^4+6z^6)}{1-z-z^4-z^6}.
\]
The exact set of *least periods* of points of \(X\) is
\[
\{1\}\cup\{n\in\mathbb N:n\ge4\};
\]
no point has least period \(2\) or \(3\). For each \(n\ge1\), the number of distinct shift orbits of least period \(n\) is
\[
O_n=\frac1n\sum_{d\mid n}\mu(n/d)P_d,
\]
where \(\mu\) is the Möbius function. The first sixteen values of \(P_n\) are
\[
2,2,2,10,12,26,30,42,56,92,134,202,288,422,612,906.
\]
This is a complete periodic-point enumeration rather than just a growth-rate estimate for finite good words.

## Assumptions and scope
A word \(u\overline u\) is an *antisquare of order* \(|u|\). The good condition permits order one only. The two-sided shift \(X\) is compact and shift invariant even though its original definition uses an infinite family of forbidden words.

The primary work of Baranwal, Currie, Mol, Ochem, Rampersad, and Shallit supplies three critical ingredients. Its Theorem 11 classifies minimal antisquares; Proposition 18 shows that a bi-infinite good word containing \(001011\) is the exceptional nonperiodic configuration \({}^{\omega}0101^{\omega}\), and bit complementation gives the analogous conclusion for \(110100\). Its Theorem 19 identifies the finite forbidden set
\[
F=\{0011,1100,0110,1001,010101,101010,001011,110100\}
\]
and proves that its avoidance is exactly the subclass of good words avoiding \(001011\) and \(110100\). It also identifies the Pansiot difference forbidden set
\[
G=\{010,101,11111,01110\}.
\]
These published classifications are assumed, not re-proved here.

A point is fixed by \(\sigma^n\) if its two-sided coordinates repeat after \(n\) positions; its *least period* may be a proper divisor of \(n\). The zeta function is interpreted formally over \(\mathbb Q[[z]]\), so no analytic convergence assumption is needed.

## Proof
**1. Periodic good points form a finite-type periodic language.** Every \(n\)-periodic good word avoids the two exceptional factors \(001011\) and \(110100\): if it contained the first, Proposition 18 would force the nonperiodic left/right eventual configuration, contradicting periodicity; the second is excluded by complementation. Theorem 19 then identifies all periodic good points with the periodic points of the finite-type binary shift avoiding precisely the eight words in \(F\). Conversely, any bi-infinite word avoiding \(F\) is good by the same theorem. Thus these two shifts have **exactly the same periodic points**, although their nonperiodic point sets need not be equal.

**2. Cyclic Pansiot codes give a two-to-one correspondence.** For a binary \(n\)-periodic word \(w\), define its cyclic difference code
\[
c_i=w_i\oplus w_{i+1},\qquad i\in\mathbb Z/n\mathbb Z.
\]
The published Pansiot coding sends avoidance of \(F\) to avoidance of the four patterns in \(G\). This equivalence also holds for cyclic configurations, since it is an equality of corresponding local forbidden windows. Conversely a cyclic binary code has a cyclic lift \(w\) if and only if the number of \(1\)'s in one period is even; when a lift exists, there are exactly two, which are complementary.

Every cyclic sequence avoiding \(G\) has an even number of \(1\)'s in its period. Indeed, the all-one sequence violates \(11111\); otherwise every maximal circular run of ones has length exactly \(2\) or \(4\). The forbidden patterns \(010\) and \(101\) forbid isolated runs, \(01110\) forbids a run of three ones, and \(11111\) forbids runs of length at least five. Hence all one-runs have even length, also when the code is all zero. Every \(n\)-periodic \(G\)-avoiding code therefore has exactly two \(n\)-periodic binary lifts. Writing \(C_n\) for the number of origin-marked, \(n\)-periodic codes avoiding \(G\), we have
\[
P_n=2C_n\quad\text{for every }n\ge1.
\]

**3. Exact transfer graph and determinant.** Use the length-four de Bruijn graph for \(G\). Its ten admissible states and complete outgoing edges (edge labels are appended bits) are

| state | outgoing labeled transitions |
| --- | --- |
| `0000` | `0:0000`, `1:0001` |
| `0001` | `1:0011` |
| `0011` | `0:0110`, `1:0111` |
| `0110` | `0:1100` |
| `0111` | `1:1111` |
| `1000` | `0:0000`, `1:0001` |
| `1001` | `1:0011` |
| `1100` | `0:1000`, `1:1001` |
| `1110` | `0:1100` |
| `1111` | `0:1110` |

Let \(A\) be the \(10\)-by-\(10\) adjacency matrix of this graph, with states in the table order. An origin-marked \(n\)-periodic code is equivalent to a closed directed walk of length \(n\) beginning at its initial length-four block. This holds even when \(n<4\) by interpreting the initial block periodically. Therefore
\[
C_n=\operatorname{tr}(A^n).
\]
Exact integer determinant expansion (reproduced by `verify.py`, using Newton identities on the displayed adjacency matrix) gives
\[
\det(I-zA)=1-z-z^4-z^6.
\]
The first ten traces, independently exposed by that computation, are
\[
1,1,1,5,6,13,15,21,28,46.
\]
As a separate finite-matrix cross-check, the length-five de Bruijn graph of the original forbidden set \(F\) has twenty allowed states and its adjacency matrix \(B\) satisfies
\[
\det(I-zB)=(1-z-z^4-z^6)^2.
\]
This independent direct binary presentation yields the same periodic-point enumerator.

**4. Rational zeta and generating function.** Over formal power series, the standard finite-matrix logarithmic determinant identity reads
\[
-\log\det(I-zA)=\sum_{n\ge1}\frac{\operatorname{tr}(A^n)}n z^n.
\]
Using \(P_n=2\operatorname{tr}(A^n)\) and exponentiating proves
\[
\zeta_X(z)=\det(I-zA)^{-2}
=(1-z-z^4-z^6)^{-2}.
\]
Logarithmic differentiation then gives the stated rational expression for \(\sum_{n\ge1}P_nz^n\). The Möbius inversion formula for exact periods follows from
\[
P_n=\sum_{d\mid n}dO_d.
\]

**5. Complete set of least periods.** Every periodic difference code either consists entirely of zeros or, if it contains ones, has a circular block of ones of length \(2\) or \(4\), followed by a circular block of at least two zeros. In particular, for \(n=2\) or \(3\), only the constant-zero difference code is possible, and its two binary lifts are the two constant sequences. For every \(n\ge4\), the circular code
\[
c=11\,0^{n-2}
\]
avoids \(G\), has two ones and exactly one circular pair of adjacent ones, so its least period is exactly \(n\). Its even parity ensures a binary cyclic lift; the lift's least period is also \(n\), since taking adjacent differences preserves any period. Both complementary lifts belong to \(X\), as shown above. This proves the exact least-period set.

## Verification
The standalone `verify.py` reconstructs the ten code states and their labeled transitions from \(G\) and determines \(\det(I-zA)\) exactly by integer Newton identities, not by floating-point approximation. Independently, it constructs the twenty-state binary graph for \(F\), computes its exact determinant, and checks that it equals the square of the code determinant. It tests the identity \(\operatorname{tr}(B^n)=2\operatorname{tr}(A^n)\) for \(1\le n\le40\).

For every \(1\le n\le16\), an independent exhaustive enumeration of all binary circular words counts \(F\)-admissible words and \(G\)-admissible codes, agreeing with both transfer graphs. For \(n\le10\), the verifier also directly checks avoidance of antisquares of orders \(2\) through \(2n+6\), without applying the finite-type shortcut. The explicit least-period witness is checked for \(4\le n\le300\). The exact matrix identities and symbolic infinite arguments, rather than these bounded enumerations, establish the theorem for all \(n\).

## Relationship to prior work
Baranwal and collaborators already classify the minimal forbidden antisquares, identify the eight-factor finite-type core \(F\), and identify its four-pattern Pansiot code \(G\). They derive a word-count recurrence with characteristic equation
\[
\lambda^6-\lambda^5-\lambda^2-1=0
\]
and prove \(\Theta(\psi^n)\) growth of finite good words, where \(\psi\) is the supergolden ratio. Those ingredients and the polynomial are explicitly credited as established.

The present claim is **not** a new proof of the finite-word growth rate or a new forbidden-set characterization. It separates nonperiodic exceptional good points from periodic ones, proves the even-parity cyclic lift property, evaluates the *full periodic orbit zeta*, and determines all least periods. A recurrence for linear finite-word counts alone does not give the trace of powers of the recurrent graph or the exact multiplicity-two cyclic lift; those additional statements and the primitive-period classification are the new contribution.

The related paper “Complement Avoidance in Binary Words” addresses the distinct property of occurrence of both a word and its complement, rather than enumerating periodic orbits in the antisquare-good shift. No inspected primary source states this zeta or its complete exact-period set.

## Limitations
The rational zeta enumerates only periodic orbits. It does not enumerate all nonperiodic sequences of \(X\), which include exceptional heteroclinic configurations, and does not assert that \(X\) itself is a shift of finite type. The finite forbidden-set equality used in the argument applies **to periodic points only**.

The paper's finite-word growth polynomial coincides with the denominator in the new zeta; the polynomial itself is published and not claimed as new. A short unindexed observation could already have taken traces of the same graph; literature searches cannot exclude that possibility. The theorem does not address periodic orbits of classes permitting larger antisquares.

## References
1. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, and J. Shallit, “Antisquares and Critical Exponents,” arXiv:2209.09223v1 (first public 2022-09-19); *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), DOI 10.46298/dmtcs.10063. Especially Theorem 11, Proposition 18, and Theorem 19.
2. J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, and J. Shallit, “Complement Avoidance in Binary Words,” arXiv:2209.09598v2. Examined for possible stronger coverage; its object and enumerative questions differ.
