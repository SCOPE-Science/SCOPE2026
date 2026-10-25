# Complete radius-one factors and entropy spectrum of the binary even shift

## Finding

Let \(X\subset\{0,1\}^{\mathbb Z}\) be the *even shift*: between successive occurrences of the symbol \(1\), the number of intervening zeros is even. Equivalently, the finite forbidden factors are \(10^{2k+1}1\), for all integers \(k\geq0\). For Wolfram's radius-one binary cellular automaton \(F_r\), define
\[
(F_r(x))_i=\left\lfloor\frac{r}{2^{4x_{i-1}+2x_i+x_{i+1}}}\right\rfloor\bmod2,\qquad 0\leq r\leq255.
\]
Exactly **16 Wolfram rules**, representing **eight distinct maps on \(X\)**, satisfy \(F_r(X)\subseteq X\):

| Map on the even shift | Wolfram codes | Image |
|---|---|---|
| Constant zero | 0, 32 | \(\{0^{\mathbb Z}\}\) |
| Constant one | 223, 255 | \(\{1^{\mathbb Z}\}\) |
| Right-coordinate shift | 138, 170 | \(X\) |
| Identity | 204, 236 | \(X\) |
| Left-coordinate shift | 208, 240 | \(X\) |
| First proper factor | 139, 171 | \(Y_A\) |
| Reflected proper factor | 209, 241 | \(Y_A\) |
| Radius-one Boolean dilation | 222, 254 | \(Y_B\) |

The two proper, nonconstant image shifts have **exact** descriptions
\[
Y_A=\{y\in\{0,1\}^{\mathbb Z}:\text{neither `000` nor `101` occurs}\},
\]
\[
Y_B=\{y\in X:\text{neither `010` nor `0110` occurs}\}.
\]
The first is a shift of finite type; the second remains strictly sofic (not of finite type). Rule 254 restricts to the Boolean OR of three neighbors on \(X\); Rule 222 agrees with it because the triple `101` is absent from \(X\). Rules 139 and 209 induce distinct maps with the same image, related by spatial reflection.

The **only surjective radius-one self-maps** of \(X\) are its three coordinate shifts. The image-entropy spectrum of the eight distinct maps is exactly
\[
0,\quad \log\lambda_B,\quad\log\lambda_A,\quad\log\varphi,
\]
where \(\varphi=(1+\sqrt5)/2\), \(\lambda_A>1\) uniquely solves
\[
\lambda_A^3-\lambda_A^2-1=0,
\]
and \(\lambda_B>1\) uniquely solves
\[
\lambda_B^5-\lambda_B^4-\lambda_B^3+\lambda_B^2-1=0.
\]
Numerically, \(\lambda_A\approx1.4655712319\) and \(\lambda_B\approx1.4432687913\); hence \(0<\log\lambda_B<\log\lambda_A<\log\varphi\). Exactly two distinct maps have zero image entropy, one has entropy \(\log\lambda_B\), two have \(\log\lambda_A\), and three have \(\log\varphi\).

## Assumptions and scope

The domain is the bilateral even shift, not the full binary shift or a finite periodic ring. The local rule is homogeneous with memory one and anticipation one, allowing a local rule to ignore some arguments. Wolfram rule codes differing only at triple `101` define the same map on this domain, since that triple is forbidden. Claims are for one spatial update, not temporal entropy or endomorphisms of larger neighborhood radius. The entropy is the spatial topological entropy of the image subshift.

## Proof

**The predecessor transducer.** Use the familiar two-state right-resolving graph of \(X\): from parity state \(E\), symbol \(0\) goes to \(O\) and symbol \(1\) loops at \(E\); from \(O\), only symbol \(0\) is allowed and goes to \(E\). Its two-letter state presentation consists of the five triples \((s,a,b)\) for which both reading \(a\) and then \(b\) is legal from \(s\). From \((s,a,b)\), a permitted next input symbol \(c\) gives an edge to \((\delta(s,a),b,c)\), labeled by the output bit of rule \(r\) on `abc`. This graph is strongly connected and essential: each finite labeled path extends bi-infinitely. Therefore its path-label language is **exactly** the set of finite words of \(F_r(X)\), not an overapproximation.

**Complete self-map census.** A finite word belongs to \(X\) if and only if a three-state deterministic word automaton (no previous one, even zeros, odd zeros) does not enter a dead state. Apply powerset determinization to the five-state output transducer, beginning with all five predecessor states, and pair the result with this word automaton. Breadth-first reachability proves \(F_r(X)\subseteq X\) precisely when no reachable pair has a nonempty predecessor subset and a dead even-shift state. Testing every one of the 256 rule tables leaves exactly the 16 codes displayed above. All 240 excluded codes have a forbidden output witness of length at most nine. Their shortest-witness length distribution is 192 at length three, 42 at length five, two at length seven, and four at length nine. Every test explores a *closed finite state space*, so its conclusion covers arbitrary output-word length.

**Exact image languages and surjectivity.** For a candidate rule, equality of output languages is decided by breadth-first search on the product of two deterministic subset automata, detecting a word accepted on exactly one side. The same method compares the output transducer to word automata that forbid specified finite patterns, and, when relevant, to the even-shift parity automaton. The exact product closures establish
\[
F_{139}(X)=F_{209}(X)=X(\{\texttt{000},\texttt{101}\}),
\quad
F_{222}(X)=X\cap X(\{\texttt{010},\texttt{0110}\}).
\]
The two-block presentation of the finite-type image \(Y_A\) has states `00`, `01`, `10`, `11`, is strongly connected, and has the `11` self-loop, so it is mixing. All other included rules have the constant or coordinate-shift images stated in the table. Comparing each image to \(X\) leaves precisely the six codes representing the three shifts. This also proves that the proper images differ from one another and from \(X\).

**Entropy.** In each output powerset automaton, every reachable nonempty subset is accepting; if \(A\) is its nonnegative integer adjacency matrix, then the count of admissible output words of length \(n\) is \(e_0^\mathsf{T}A^n\mathbf1\). Thus the entropy equals \(\log\rho(A)\). The exact characteristic polynomials of the complete reachable matrices, computed by integer characteristic-polynomial recurrence, are
\[
\begin{aligned}
\chi_{139}(t)&=t^3(t-1)(t+1)(t^3-t^2-1),\\
\chi_{209}(t)&=t^3(t^3-t^2-1),\\
\chi_{222}(t)&=t^2(t-1)(t^5-t^4-t^3+t^2-1).
\end{aligned}
\]
Each has one spectral root above one. The first nontrivial polynomial is \(t^2(t-1)-1\), the second is \(t^2(t-1)^2(t+1)-1\), both strictly increasing for \(t>1\), with a unique zero there. The other strongly connected components have spectral radius at most one. Perron–Frobenius then yields the claimed positive dominant eigenvalues. The even shift's standard parity graph has spectral radius \(\varphi\), and a singleton image has entropy zero.

**Strict soficness of \(Y_B\).** For arbitrarily long odd and even zero gaps, the periodic words \((1110^{2m+1})^{\mathbb Z}\) and \((1110^{2m})^{\mathbb Z}\) obey the same fixed-length constraints `010`, `0110`; the latter lies in \(Y_B\), while the former violates the even-gap condition. Given any finite observation length \(L\), take \(m\) sufficiently large that both periodic words have the same factors of length at most \(L\). Hence no finite forbidden list describes \(Y_B\). The finite transducer proves it is sofic.

## Verification

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The checker reconstructs the full five-state transducer, exhausts all 256 rule tables, verifies the exact two image-language equalities and the onto classification, checks exact integer characteristic polynomials, and independently enumerates every output word of length one through eight from admissible finite input words for eight representative codes. Finite enumeration is a cross-check only; the unrestricted statements follow from complete subset-state closure. The checker reports `VERIFY_OK` when all assertions hold.

## Relationship to prior work

Béal, Berstel, Eilers and Perrin describe the even shift, its strict soficness, sliding-block maps, and finite labeled automata; their general presentation supplies the standard machinery used here. Salo's work investigates quite different realization questions about nonuniform cellular automata and includes a general discussion of maps over sofic shifts. The present specific eight-map census, exact two image languages, radius-one onto rigidity, and paired entropy polynomials are not stated in the inspected relevant portions of those works. This is a statement-level comparison, not a claim that a keyword search proves priority.

## Limitations

No assertion is made about centered radius two or higher, all endomorphisms of \(X\), or temporal behavior under repeated updates. The original literature may contain an earlier equivalent radius-one table or these algebraic entropy values under another notation; an independent historical-priority audit is still needed. The numerical values serve only as orientation and are not proof of the algebraic root identities.

## References

- M.-P. Béal, J. Berstel, S. Eilers, D. Perrin, *Symbolic dynamics*, arXiv:1006.1265v1 (first publicly posted 2010-06-07), especially Sections 2.1, 2.2, 3.1; https://arxiv.org/abs/1006.1265.
- V. Salo, *Realization problems for nonuniform cellular automata*, *Theoretical Computer Science* **559** (2014), 91–107, DOI:10.1016/j.tcs.2014.07.031; especially the introduction and discussion of nonuniform CA over sofic shifts.
