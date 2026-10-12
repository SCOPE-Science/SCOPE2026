# A local conservation law for lower-plus-upper Wythoff representations
## Finding
Let \(\varphi=(1+\sqrt5)/2\), and define the lower and upper Wythoff sequences by
\[
u(h)=\lfloor h\varphi\rfloor,\qquad v(k)=\lfloor k\varphi^2\rfloor
\]
for integers \(h,k\ge1\). Define
\[
r(n)=\#\{(h,k)\in\mathbb Z_{\ge1}^2:u(h)+v(k)=n\}.
\]
For every integer \(t\ge1\), write
\[
\tau_t=\{t\varphi^2\},\qquad
A_t=\#\{1\le j<t:\{j\varphi^2\}<\tau_t\}.
\]
Then
\[
r(v(t)-1)=A_t,\qquad r(v(t))=t-1-A_t.
\]
Consequently,
\[
r(v(t)-1)+r(v(t))=t-1
\]
for every \(t\ge1\). In particular,
\[
\max\{r(v(t)-1),r(v(t))\}\ge \frac{t-1}2,
\]
so the representation multiplicity is forced to grow without bound along these natural adjacent pairs.

## Assumptions and scope
All indices are positive integers. Fractional parts are denoted by \(\{x\}\). The theorem concerns the exact representation function A259598, not merely membership in the sumset of the lower and upper Wythoff sequences.

The proof uses Beatty complementarity for \(\varphi\) and \(\varphi^2\): the two sequences \(u(1),u(2),\ldots\) and \(v(1),v(2),\ldots\) partition the positive integers. No finite experiment is used to prove the infinite statement.

## Proof
Put \(\alpha=\varphi^2\). For an integer \(n\ge1\), let
\[
K(n)=\#\{k\ge1:v(k)<n\},
\]
and let
\[
s(n)=\#\{(j,k)\in\mathbb Z_{\ge1}^2:v(j)+v(k)=n\}.
\]
For every \(k\) counted by \(K(n)\), the positive remainder \(n-v(k)\) lies in exactly one of the complementary Beatty sequences. It contributes to \(r(n)\) exactly when that remainder is lower Wythoff; otherwise it is uniquely \(v(j)\) for some \(j\). Hence
\[
r(n)=K(n)-s(n). \tag{1}
\]
Since \(v(k)=\lfloor k\alpha\rfloor\) and \(n\) is integral,
\[
v(k)<n\quad\Longleftrightarrow\quad k\alpha<n,
\]
so
\[
K(n)=\left\lfloor\frac n\alpha\right\rfloor. \tag{2}
\]

Fix \(t\ge1\), put \(N=v(t)=\lfloor t\alpha\rfloor\), and write \(\tau=\{t\alpha\}\). Because \(2<\alpha<3\), consecutive values of \(v\) differ by either \(2\) or \(3\). Formula (2) therefore gives
\[
K(N)=K(N-1)=t-1. \tag{3}
\]

We next classify the upper-plus-upper representations of \(N\) and \(N-1\). If \(j+k=q\), then
\[
v(j)+v(k)\in\{v(q)-1,v(q)\}.
\]
If \(q\le t-1\), this sum is at most \(v(t-1)\le N-2\); if \(q\ge t+1\), it is at least \(v(t+1)-1\ge N+1\). Thus any representation of either \(N\) or \(N-1\) must have
\[
j+k=t. \tag{4}
\]

For \(1\le j<t\), set \(k=t-j\). Irrationality of \(\alpha\) makes \(\{j\alpha\}\ne\tau\). If \(\{j\alpha\}<\tau\), then
\[
\{k\alpha\}=\tau-\{j\alpha\},
\]
so there is no carry and \(v(j)+v(k)=N\). If \(\{j\alpha\}>\tau\), then
\[
\{k\alpha\}=1+\tau-\{j\alpha\},
\]
so there is one carry and \(v(j)+v(k)=N-1\). Therefore
\[
s(N)=A_t,\qquad s(N-1)=t-1-A_t. \tag{5}
\]
Combining (1), (3), and (5) gives
\[
r(N)=t-1-A_t,\qquad r(N-1)=A_t,
\]
which proves the theorem.

## Verification
The bundled script `verify.py` reconstructs \(u\), \(v\), and \(r\) using exact integer arithmetic. It checks the two exact formulas and their sum for every \(1\le t\le1000\). The finite replay is corroborative only; the proof above establishes all \(t\ge1\).

## Relationship to prior work
Ashburn's 2026 note studies this exact representation function and proves the complete fibers \(r(n)=0\), \(r(n)=1\), and \(r(n)=2\). The present conservation law instead controls a natural infinite family of adjacent pairs for arbitrary representation multiplicity and is not stated in the inspected note.

The OEIS entry A259598 defines the same representation function, gives its generating function, and records the three low-fiber conjectures, but the inspected entry does not state the adjacent-pair identity. Shallit's earlier paper proves sumset-membership statements for lower and upper Wythoff sequences by automata; its inspected Wythoff section determines whether a representation exists, not the exact local multiplicity conservation law above.

## Limitations
The theorem determines the sum of the two adjacent multiplicities exactly, but it does not give a closed form for the individual rank \(A_t\) beyond its irrational-rotation definition. It does not classify all level sets \(r(n)=m\) for arbitrary \(m\), nor does it replace the broader asymptotic description of \(r(n)\).

The originality comparison covered the direct 2026 source, the current OEIS entry, Shallit's full Wythoff-sumset treatment, and targeted semantic searches for the exact identity and equivalent formulations. A differently phrased identity in older Beatty-sequence literature remains a residual literature-search risk.

## References
1. Alex Ashburn, "Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words," arXiv:2610.04842v1, 4 October 2026. Section 3 treats A259598 and its fibers of multiplicity \(0\), \(1\), and \(2\).
2. OEIS A259598, "Number of representations of n as u(h) + v(k)," current entry inspected in October 2026.
3. Jeffrey Shallit, "Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond," arXiv:2006.04177v1; later *Periodica Mathematica Hungarica* 83 (2021), 37-46.
