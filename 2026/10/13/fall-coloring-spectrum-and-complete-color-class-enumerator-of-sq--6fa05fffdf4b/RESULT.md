# Fall-coloring spectrum and complete color-class enumerator of squared cycles

## Finding
For every integer \(n\ge7\), write \(G_n=C_n^2\) for the graph on \(\mathbb Z/n\mathbb Z\) in which vertices at cyclic distance \(1\) or \(2\) are adjacent. A *fall \(q\)-coloring* is a partition into \(q\) nonempty independent color classes such that every vertex has a neighbor in each of the other \(q-1\) classes. The classes, not color labels, are counted once. Let \(P_n(z)=\sum_{q\ge1}p_{n,q}z^q\) count these partitions by number of classes.

**Theorem.** For all \(n\ge7\),
\[
P_n(z)={\bf1}_{3\mid n}z^3+\frac{F_n}{24}z^4+{\bf1}_{5\mid n}z^5,
\]
where \(F_n\) is specified for every positive integer by the exact rational generating function
\[
\sum_{n\ge1}F_nt^n=-t\frac{D'(t)}{D(t)},
\]
and
\[
\begin{aligned}
D(t)={}&(1-t)^5(1-t-t^2)(1+t+t^2)^4\\
&\cdot(1-t+t^3)^3(1+t+t^3)^2\\
&\cdot(1+t+2t^2+2t^3+t^4+t^6)^3.
\end{aligned}
\]
In particular, a fall four-coloring exists if and only if \(n\notin\{7,11\}\); a fall three-coloring exists if and only if \(3\mid n\); and a fall five-coloring exists if and only if \(5\mid n\). Hence the only \(n\ge7\) with no fall coloring are \(7\) and \(11\). The four-class partition counts for orders \(7\) through \(15\) are respectively \(0,7,3,5,0,31,13,35,20\).

## Assumptions and scope
All graphs are finite and simple. The domain is the **entire infinite family** of squared cycles of orders \(n\ge7\). Color classes are nonempty and unlabeled; when a fixed four-color palette is used for the transfer matrix, exactly \(4!=24\) labeled colorings represent each unlabelled partition. The generating function defining \(F_n\) is formal in \(t\); its coefficients for \(n<7\) are auxiliary trace values, not asserted to enumerate fall colorings of small squared cycles. For \(n\ge7\), the graph is four-regular and contains a triangle, so a fall coloring can use only \(3,4\), or \(5\) colors.

## Proof
**Three and five classes.** With three colors, every three consecutive cyclic vertices must have pairwise different colors. This forces the cyclic word to repeat with period three, so \(3\mid n\), and conversely this repetition gives a fall coloring. Up to permutation of color names, it is unique. For five colors, the closed neighborhood of a vertex consists of five vertices and must have five distinct colors. Every cyclic window of length five therefore contains all five colors; consecutive windows force period five, so \(5\mid n\). Conversely the repeated five-letter word is a fall coloring and is unique up to palette permutation. The five-color existence criterion is also the case \(k=2\) of the maximum fall-achromatic-number result of Kumar, Nicholas and Somasundaram (2011); it is **not** claimed separately as new.

**Four classes and the transfer.** Use a fixed palette \(\{0,1,2,3\}\). A cyclic word \((a_i)_{i\in\mathbb Z/n\mathbb Z}\) is a fall four-coloring exactly when every consecutive triple consists of three distinct letters and every consecutive five-letter window contains four distinct letters. Indeed, the triple condition is properness for the square of the cycle, while the five-letter condition says that the center vertex has a neighbor in all three other classes.

Form the set \(Q\) of the \(48\) quadruples \((a,b,c,d)\in\{0,1,2,3\}^4\) for which \(a,b,c\) are pairwise distinct and \(b,c,d\) are pairwise distinct. Define the integer matrix \(T\), indexed by \(Q\), by
\[
T_{(a,b,c,d),(b,c,d,e)}=
\begin{cases}1,&e\notin\{c,d\}\text{ and }|\{a,b,c,d,e\}|=4,\\0,&\text{otherwise};\end{cases}
\]
all other entries being zero. Starting the length-four state at each cyclic vertex gives a bijection between indexed cyclic fall four-colorings and closed walks of length \(n\) in this directed state graph. Thus \(F_n=\operatorname{tr}(T^n)\) for every \(n\ge7\).

An exact determinant evaluation gives \(\det(I-tT)=D(t)\), with \(D(t)\) factored as in the theorem. For a fully reproducible finite algebraic certificate, `verify.py` constructs the \(48\) states and transition edges from the definition, computes \(s_j=\operatorname{tr}(T^j)\) exactly for \(1\le j\le48\), and computes the coefficients \(c_0=1\),
\[
c_k=-\frac1k\sum_{j=1}^k c_{k-j}s_j\qquad(1\le k\le48).
\]
Newton's identities guarantee \(\det(I-tT)=\sum_{k=0}^{48}c_kt^k\); the certificate checks exact equality with the stated degree-\(48\) factorization. The formal trace-determinant identity then proves \(\sum_{n\ge1}\operatorname{tr}(T^n)t^n=-tD'(t)/D(t)\). All four colors appear in a fall four-coloring, and the palette permutation group acts freely, so the unlabeled count is \(F_n/24\).

**Existence and its exceptional orders.** The determinant formula gives \(F_7=F_{11}=0\). The four cyclic words, whose digits represent four distinct colors,

- `01203123` (length \(8\)),
- `012031023` (length \(9\)),
- `0120310213` (length \(10\)), and
- `012031021320123` (length \(15\))

all pass the cyclic three- and five-window conditions. In every fall four-coloring, some four consecutive positions must have pairwise different colors: otherwise every fourth color would equal the first of its four-window (the triple condition excludes the middle two), forcing a period-three word with only three colors. If \(a,b,c,d\) are four consecutive distinct colors, inserting a second copy of \(a,b,c,d\) immediately after them produces a cyclic word of length \(n+4\) satisfying the same conditions. Every newly created five-window contains all four letters, and the original windows outside the insertion are unchanged. Inducting by four from the four displayed orders yields every order \(n\ge8\) other than \(11\). Together with \(F_7=F_{11}=0\), this proves the claimed exact four-color fall spectrum. Combining it with the three- and five-color cases proves the theorem.

## Verification
Run `python3 verify.py` using Python 3 standard library. It constructs \(T\), verifies the stated degree-\(48\) characteristic determinant by exact integer Newton identities, computes \(\operatorname{tr}(T^n)\) through order \(64\), compares these values with an independent direct-coloring enumeration for all orders \(7\) through \(16\), checks all four witnesses and the zero orders \(7\) and \(11\), and checks divisibility by \(24\). Expected terminal line: `VERIFY_OK states=48 characteristic_degree=48 matrix_trace_orders=1..64 independently_bruteforced_orders=7..16 exceptional_orders=7,11 witnesses=8,9,10,15`. The infinite theorem does not rely on finite enumeration alone: it uses the closed-walk bijection, determinant identity, and insertion argument.

## Relationship to prior work
Kumar, Nicholas and Somasundaram (2011, Theorem 6) establish the fall \(\Delta+1\)-coloring divisibility criterion for powers of cycles. For the square this supplies the already-known five-color presence criterion, but not the fall four-color counts, its rational enumerator, or the exceptional non-fall-colorable orders. Dunbar and collaborators (2000) introduce the fall-coloring framework. Wang and collaborators (2024) prove general density bounds and complexity/existence statements for fall-colorable graphs, without the exact squared-cycle fall-coloring enumeration. In particular, a proper four-coloring or a general \(b\)-coloring is not the all-vertices-colorful condition used here. Comparisons do not establish universal priority; a disguised equivalent enumeration could remain in the literature.

## Limitations
The counting formula is restricted to ordinary undirected squared cycles with \(n\ge7\), and does not treat higher cycle powers or other graph products. The finite verifier tests a bounded set of orders; the unrestricted claims depend on the explicit combinatorial proof and reproducible exact matrix determinant. These results have not undergone independent mathematical audit, and possible alternative pre-existing terminology remains an originality risk.

## References
1. S. Chandra Kumar, T. Nicholas and S. Somasundaram, *Fall Coloring on Product of Cycles and Powers*, Journal of Mathematics Research **3**(4), 152–156 (2011), DOI: 10.5539/jmr.v3n4p152. First published 1 November 2011. [Full text](https://pdfs.semanticscholar.org/1804/e9edfbab788cf4ad1aae7ad4251c9fd684f0.pdf).
2. J. E. Dunbar et al., *Fall Colorings of Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **33**, 257–273 (2000). [Open text](https://combinatorialpress.com/jcmcc-articles/volume-033/fall-colorings-of-graphs/).
3. S. Wang, F. Wen, G. Wang and Z. Li, *On Fall-Colorable Graphs*, Mathematics **12**, 1105 (2024), DOI: 10.3390/math12071105.
