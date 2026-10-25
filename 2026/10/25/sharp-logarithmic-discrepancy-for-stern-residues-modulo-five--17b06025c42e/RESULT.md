# Sharp logarithmic discrepancy for Stern residues modulo five

## Finding

Let \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\) for \(n\geq1\). Define the signed residue discrepancy at every integer \(N\geq0\) by
\[
D(N)=\#\{0\leq n<N:s(n)\equiv1\pmod5\}-\#\{0\leq n<N:s(n)\equiv4\pmod5\}.
\]
For each \(r\geq0\), let \(M_r=\max_{0\leq N\leq2^r}D(N)\) and \(m_r=\min_{0\leq N\leq2^r}D(N)\). Then **for every integer \(r\geq8\)**,
\[
\boxed{M_{r+12}=M_r+4,\qquad m_{r+12}=m_r-4.}
\]
In order for \(r=8,9,\ldots,19\), the twelve base values are
\[
(M_r)=(7,7,7,7,8,8,8,8,9,9,9,9),
\quad
(m_r)=(-1,-1,-2,-2,-2,-2,-4,-4,-4,-4,-5,-5).
\]
Consequently \(M_r=r/3+O(1)\), \(m_r=-r/3+O(1)\), and
\[
\boxed{\limsup_{N\to\infty}\frac{D(N)}{\log_2 N}=\frac13,
\qquad\liminf_{N\to\infty}\frac{D(N)}{\log_2 N}=-\frac13.}
\]
Two explicit departures from the early observed range are \(D(2190712)=-6\) and \(D(8693112)=12\).

## Assumptions and scope

All counts are over integer indices; every prefix includes the empty prefix at \(N=0\). The congruence modulus is exactly five, with residues represented by \(0,1,2,3,4\). The twelve-step identity holds for all \(r\geq8\), not merely selected dyadic scales. The statement makes no claim about other moduli or pointwise limits of \(D(N)\).

## Proof

Put \(Q=\mathbb F_5^2\setminus\{(0,0)\}\) (24 states), and define \(w(a)=\mathbf1_{a=1}-\mathbf1_{a=4}\) for \(a\in\mathbb F_5\). For each state \(v=(a,b)\), set
\[
L(a,b)=(a,a+b),\qquad R(a,b)=(a+b,b),
\]
with coordinates reduced modulo five. The transformations are invertible, so they preserve \(Q\). Stern's defining recurrence gives the exact pair identities
\[
(s(2n),s(2n+1))=L(s(n),s(n+1)),\quad
(s(2n+1),s(2n+2))=R(s(n),s(n+1)).
\]
Let \(W_r(v)\) be the length-\(2^r\) integer word formed by taking all binary words of length \(r\) in lexicographic order, applying their successive \(L\) and \(R\) transformations to \(v\), and recording \(w\) of the first coordinate. Therefore
\[
W_0(a,b)=(w(a)),\qquad W_{r+1}(v)=W_r(Lv)\mathbin\Vert W_r(Rv),
\]
where \(\Vert\) denotes concatenation. Starting at \(v_0=(0,1)\), the leading-zero-compatible Stern recursion implies
\[
W_r(v_0)=(w(s(0)),w(s(1)),\ldots,w(s(2^r-1))).
\]

For each \(v\in Q\), let \(S_r(v)\) be the sum of the letters of \(W_r(v)\); let \(H_r(v)\) and \(J_r(v)\) be the largest and smallest prefix sums, with empty prefix included. At depth zero,
\[
S_0(a,b)=w(a),\quad H_0(a,b)=\max(0,w(a)),\quad J_0(a,b)=\min(0,w(a)).
\]
Concatenation gives the **exact integer** recurrences
\[
\begin{aligned}
S_{r+1}(v)&=S_r(Lv)+S_r(Rv),\\
H_{r+1}(v)&=\max\{H_r(Lv),S_r(Lv)+H_r(Rv)\},\\
J_{r+1}(v)&=\min\{J_r(Lv),S_r(Lv)+J_r(Rv)\}.
\end{aligned}
\]
These are identities for all possible prefixes, not approximations.

The attached table `CERTIFICATE.csv` supplies, for **all 24 states**, the exact integer triples \((S_{16},H_{16},J_{16})\) and \((S_{28},H_{28},J_{28})\). Applying the displayed recurrences to its 24 states (or independently running `verify.py` from the initial depth-zero table) proves the finite certificate
\[
\forall v\in Q:\quad
S_{28}(v)=S_{16}(v),\quad
H_{28}(v)=H_{16}(v)+4,\quad
J_{28}(v)=J_{16}(v)-4.
\]
Because each update uses only sums, maximum, and minimum, this **simultaneous 24-state** identity propagates inductively: for example,
\[
H_{29}(v)=\max\{H_{28}(Lv),S_{28}(Lv)+H_{28}(Rv)\}=H_{17}(v)+4,
\]
with identical propagation for \(S\) and \(J\). Thus the identities at depths \(r\) and \(r+12\) hold for every state for all \(r\geq16\). The exact computation for the root \(v_0\) at the eight depths \(8\leq r\leq15\), recorded by `verify.py`, also gives the required shift at \(r+12\). The twelve displayed base extrema cover the remaining cases. Since \(M_r=H_r(v_0)\) and \(m_r=J_r(v_0)\), the sharp twelve-step recurrence follows for all \(r\geq8\).

The recurrence yields \(M_r=r/3+O(1)\) and \(m_r=-r/3+O(1)\). For \(N\geq2\), choose \(r=\lceil\log_2N\rceil\), giving \(m_r\leq D(N)\leq M_r\) and hence both bounds on normalized limit superior and inferior. Conversely choose a maximizing index \(N_r\leq2^r\) for each \(r\); then \(D(N_r)=M_r\to\infty\), so \(N_r\to\infty\), and \(\log_2N_r\leq r\) yields a limit-superior lower bound \(1/3\). Minimizing indices yield the matching limit-inferior upper bound \(-1/3\). The explicit witness discrepancies follow by exact binary-block prefix summation from the same defining recurrence.

## Verification

Run `python3 verify.py` alongside `CERTIFICATE.csv` (Python 3 standard library only). It recomputes the finite 24-state depth-16/depth-28 certificate from the depth-zero definitions, checks all twelve base values and eight bridging identities, checks 16384 prefixes against direct integer Stern terms, independently evaluates two distant discrepancy witnesses via binary block sums, and checks the certificate table. The finite certificate plus algebraic induction is the proof for all depths; enumeration of individual Stern terms alone would not establish it.

## Relationship to prior work

Bruce Reznick's *Regularity properties of the Stern enumeration of the rationals* (arXiv:math/0610601v1, Sections 4–5) establishes modular equidistribution and a bounded signed discrepancy for modulus three. Its closing discussion reports only a **finite Mathematica observation** that \(-5\leq D(N)\leq11\) for \(N\leq2^{19}\) when the modulus is five, without asserting that the same bound holds for all \(N\). The present theorem establishes the exact, unbounded modulo-five behavior and is consistent with that finite observation. The later treatment by J.-P. Allouche (arXiv:1202.4171) develops Stern/twisted-Stern identities rather than this signed modular-prefix extremum law.

## Limitations

The theorem concerns only the signed difference between residue classes one and four modulo five; it does not determine every individual residue-class error or more general moduli. The archival bibliographic search did not locate the full 2012 class notes *A Stern introduction to combinatorial number theory*, which could contain related or stronger results. An unlocated equivalent theorem remains a priority risk; independent mathematical and priority review have not been performed.

## References

1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601v1 (first public submission 19 October 2006), especially Section 5. https://arxiv.org/html/math/0610601v1
2. J.-P. Allouche, *On the Stern sequence and its twisted version*, arXiv:1202.4171 (2012). https://arxiv.org/abs/1202.4171
3. OEIS A002487, *Stern's diatomic series*. https://oeis.org/A002487
