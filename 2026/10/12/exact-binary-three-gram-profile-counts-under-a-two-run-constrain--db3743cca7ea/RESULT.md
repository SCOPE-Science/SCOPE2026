# Exact binary three-gram profile counts under a two-run constraint

## Finding
For every integer \(n\ge 2\), let \(W_n\) be the binary strings of length \(n\) avoiding the factors \(000\) and \(111\) (equivalently, every constant run has length at most two). Let \(p_3(w)\) be the vector of occurrence multiplicities of the six permitted contiguous three-grams, in the order \((001,010,011,100,101,110)\). Write
\[
M(n)=|\{p_3(w):w\in W_n\}|.
\]
Then, with \(m=n-2\), the exact generating function is
\[
\boxed{\sum_{n\ge2} M(n)z^{n-2}=\frac{1+6z+8z^2+5z^3+4z^4+2z^5}{(1-z^2)(1-z^3)(1-z^4)}.}
\]
In particular, for all \(n\ge2\),
\[
\boxed{M(n)=\frac{13}{24}m^2+\frac94m+\gamma_{m\bmod12}},\qquad m=n-2,
\]
where the twelve constants, listed in residue order \(0,1,\ldots,11\), are
\[
(1,\tfrac{77}{24},\tfrac73,\tfrac38,\tfrac73,\tfrac{77}{24},1,\tfrac{41}{24},\tfrac73,\tfrac{15}{8},\tfrac73,\tfrac{41}{24}).
\]
The quasipolynomial has **minimal period twelve**, and therefore \(M(n)=\frac{13}{24}n^2+O(n)\). Equivalently, \(M(n)\) is the maximum cardinality of a zero-error code inside \(W_n\) when the receiver observes the *complete multiplicity-preserving three-gram spectrum* without errors.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), only contiguous three-grams are counted, and their multiplicities—not merely their presence—are retained. No cyclic wraparound grams are included. Each string has length \(n\ge2\); at \(n=2\) the empty three-gram profile is unique, so \(M(2)=1\). The constraint is precisely avoidance of the two length-three homopolymers. The statement makes no assertion about partial, noisy or missing spectra or about identifying *every* admissible string uniquely.

## Proof
Put \(m=n-2\). A length-\(n\) word is a directed walk of \(m\) edges in the restricted order-two de Bruijn graph on vertices \(00,01,10,11\). Label its six edges by their three-grams:

| count | edge | directed transition |
|---|---|---|
| \(a\) | \(001\) | \(00\to01\) |
| \(b\) | \(010\) | \(01\to10\) |
| \(c\) | \(011\) | \(01\to11\) |
| \(d\) | \(100\) | \(10\to00\) |
| \(e\) | \(101\) | \(10\to01\) |
| \(f\) | \(110\) | \(11\to10\) |

The observed profile is exactly \((a,b,c,d,e,f)\). Its total edge count is \(m\). If the path starts at vertex \(s\) and ends at \(t\), its outdegree-minus-indegree vector, in vertex order \((00,01,10,11)\), equals \({\bf1}_s-{\bf1}_t\), that is
\[
(a-d,\; b+c-a-e,\; d+e-b-f,\; f-c)={\bf1}_s-{\bf1}_t.
\]
On this particular graph, nonnegative integer solutions of these equations are not merely necessary but sufficient for a walk: all positive edges of a balanced solution meet the central vertices \(01,10\) in one connected support, and the same holds for an imbalance from \(01\) to \(10\). Indeed, balanced solutions have the form
\[
(a,b,c,d,e,f)=(A,B,C,A,B+C-A,C),\quad A,B,C\ge0,\ A\le B+C.
\]
Any nonzero such solution has connected underlying positive-edge support: a positive \(A\) supplies \(10\to00\to01\), a positive \(C\) supplies \(01\to11\to10\), and a positive \(B\) directly joins \(01\to10\). An imbalance \(01\to10\) instead gives
\[
(a,b,c,d,e,f)=(A,B,C,A,B+C-A-1,C),\quad A,B,C\ge0,\ A\le B+C-1,
\]
and hence \(B+C\ge1\): it contains either the direct edge \(01\to10\) or the two-edge route via \(11\). Other positive edges connect to this route. For the reverse central imbalance \(10\to01\), the same property follows by exchanging binary symbols. In each case the directed Euler trail criterion therefore supplies the desired word. The empty balanced vector is realized by any length-two word.

Every remaining endpoint imbalance is represented **uniquely as a nonnegative shift** of one of the preceding two types. Four endpoint pairs \(00\to01,01\to11,10\to00,11\to10\) subtract one of the outer edge vectors \(a,c,d,f\), respectively, and leave a balanced profile. Two pairs \(00\to11\) and \(11\to00\) subtract \(a+c\) and \(f+d\) and leave balanced profiles. Four pairs \(00\to10,01\to00,10\to11,11\to01\) subtract, respectively, \(a,d,c,f\) and leave a central profile of type \(01\to10,01\to10,10\to01,10\to01\). The subtracted entries are forced positive by the endpoint equations; all shifts preserve connectivity. These twelve distinct start/end imbalances cannot cause double counting, because the imbalance vector determines the ordered endpoints when they differ; all four coincident-endpoint cases share exactly the same balanced profile set.

Let \(H_0(z)\) enumerate balanced profiles by total count, and \(H_c(z)\) enumerate profiles of central type \(01\to10\); by symbol complementation the other central type has the same series. Since \(a+d=2A\), \(c+f=2C\), and \(b+e=2B+C-A\), both families have total degree \(A+3C+2B\) in the balanced case and \(A+3C+2B-1\) in the central case. Thus
\[
\begin{aligned}
H_0(z)&=\sum_{B,C\ge0}\sum_{A=0}^{B+C}z^{A+3C+2B}\\
&=\frac{1}{1-z}\left[\frac{1}{(1-z^2)(1-z^3)}-\frac{z}{(1-z^3)(1-z^4)}\right]\\
&=\frac{1+z^3}{(1-z^2)(1-z^3)(1-z^4)},\\
H_c(z)&=\sum_{B+C\ge1}\sum_{A=0}^{B+C-1}z^{A+3C+2B-1}\\
&=\frac{z^{-1}}{1-z}\left[\frac{1}{(1-z^2)(1-z^3)}-\frac{1}{(1-z^3)(1-z^4)}\right]\\
&=\frac{z(1+z)}{(1-z^2)(1-z^3)(1-z^4)}.
\end{aligned}
\]
The endpoint decomposition now yields the exact identity
\[
\sum_{n\ge2}M(n)z^{n-2}=(1+4z+2z^2)H_0(z)+(2+4z)H_c(z),
\]
whose numerator expands to \(1+6z+8z^2+5z^3+4z^4+2z^5\), proving the generating function.

To extract coefficients, partial fractions at the roots of unity give
\[
\frac{1+6z+8z^2+5z^3+4z^4+2z^5}{(1-z^2)(1-z^3)(1-z^4)}
=\frac{13}{12(1-z)^3}+\frac{5}{8(1-z)^2}+\frac{35}{144(1-z)}
-\frac{1}{16(z+1)}-\frac{4(z+2)}{9(z^2+z+1)}+\frac{3z}{4(z^2+1)}.
\]
The pole at \(1\) yields exactly \(\frac{13}{24}m^2+\frac94m+\frac{281}{144}\); the three remaining terms yield the displayed twelve-valued bounded periodic correction. The nonzero third- and fourth-root terms ensure a minimal period divisible by both \(3\) and \(4\), hence exactly \(12\).

## Verification
Run `python3 verify_profiles.py` using Python 3 standard library. The program independently constructs all path-profile sets through \(m=72\) by directed-walk dynamic programming, matches every coefficient from the rational generating function, independently enumerates every feasible start/end degree imbalance through \(m=40\), and directly enumerates every permitted binary string through \(n=17\). The precise output is recorded in `VERIFICATION.md`. These finite checks corroborate the formulas; the all-length result is established by the preceding Eulerian classification and formal-power-series identities rather than extrapolation from finite tests.

## Relationship to prior work
Kiah, Puleo and Milenkovic introduced multiplicity-preserving sequence profiles and restricted de Bruijn graph enumeration. Their expanded full text, *Codes for DNA Sequence Profiles* (arXiv:1410.8837v2, Sections 2, 4, 5 and 7), encompasses the family \(S(2,3;1,[1,2])\) as a special restricted graph and establishes the generic growth degree \(|S|-|V(S)|=2\) using Ehrhart methods. Their numerical table of restricted weights (Table II) starts at gram length four and does **not** tabulate the present exact length-three, six-edge rational series, its \(13/24\) leading coefficient or twelve-residue formula. Thus the general graph formalism and quadratic growth degree are **prior work**; the precise all-length enumeration is the contribution here. Earlier results on complete unrestricted binary three-gram profiles, including leading term \(n^4/288\), likewise do not imply the homopolymer-constrained coefficient. The related binary two-gram constrained enumerator answers a different observation model and does not determine the three-gram spectrum.

## Limitations
This theorem assumes complete noiseless access to gram multiplicities and is not a decoding or error-correction bound for incomplete sequencing reads. It counts distinguishable profiles, not the number of admissible strings with unique profiles. No similar closed expression is claimed for larger alphabets, higher gram lengths, or other run constraints. Earlier unknown specialized enumerations remain a bibliographic possibility; no assertion of absolute historical priority is made.

## References
1. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837, initially submitted 2014-10-31; expanded as *Codes for DNA Sequence Profiles*, arXiv:1410.8837v2 (2015). https://arxiv.org/abs/1410.8837 ; full text https://arxiv.org/html/1410.8837v2.
2. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517, initially submitted 2015-02-02. https://arxiv.org/abs/1502.00517.
