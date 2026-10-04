# Sharp modal threshold at the repeated-root trace-one recurrence
## Finding
Let \(G_0=0\), \(G_1=1\), and
\[
G_{n+2}=G_{n+1}-\frac14G_n.
\]
At the repeated root this gives \(G_n=n2^{1-n}\). Set \(h=3/4\), \(a_j=G_{2j}+G_j\), and, for even \(N\ge4\) and \(1\le j\le N-2\), set
\[
T_{N,j}=N\binom{N-1}{j}h^{N-j}a_j\zeta(j+1-N).
\]
Every odd-indexed term is zero. Among the nonzero terms, the unique maximizing index of \(\lvert T_{N,j}\rvert\) is \(2\) at \(N=4\), \(4\) at \(N=6\), \(6\) at \(N=8\), and \(4\) for every even \(N\ge10\). Thus the smallest even permanent-mode threshold is \(N_0=10\).

## Assumptions and scope
The recurrence is the \(q=1/4\) repeated-root specialization of the trace-one family \(X_{j+2}=X_{j+1}-qX_j\), with the initial values \(G_0=0\), \(G_1=1\). The scale is \(h=1-q=3/4\), and the weights are the corresponding \(a_j=G_{2j}+G_j\). The statement concerns even \(N\ge4\) only. It does not assert a uniform neighborhood in \(q\), and it does not concern the distinct Fibonacci--Lucas specialization \(q=-1\).

## Proof
Danesh's trace-one recurrence identity gives the displayed summands at \(q=1/4\), and the repeated-root formula in the same source gives
\[
G_j=j2^{1-j},\qquad a_j=j2^{1-j}(1+2^{1-j}).
\]
If \(j\) is odd, then \(j+1-N\) is a negative even integer, so the corresponding zeta value is zero. Let \(j\) be even and write \(m=N-j\ge2\). Euler's formula for positive even zeta values gives
\[
\lvert T_{N,j}\rvert
=2N!\left(\frac{h}{2\pi}\right)^N\omega_j\zeta(N-j),
\qquad
\omega_j=\frac{a_j}{j!}\left(\frac{2\pi}{h}\right)^j.
\]
At \(h=3/4\),
\[
\omega_j=\frac{2(4\pi/3)^j(1+2^{1-j})}{(j-1)!},
\]
and hence
\[
R_j:=\frac{\omega_{j+2}}{\omega_j}
=\frac{16\pi^2}{9j(j+1)}
\frac{1+2^{-j-1}}{1+2^{1-j}}.
\]
In particular,
\[
R_2=\frac{2\pi^2}9>1,
\qquad
R_4=\frac{11\pi^2}{135},
\]
while for every even \(j\ge6\),
\[
R_j<\frac{16\pi^2}{9j(j+1)}\le\frac{8\pi^2}{189}.
\]
The adjacent finite-degree ratio is
\[
\frac{\lvert T_{N,j+2}\rvert}{\lvert T_{N,j}\rvert}
=R_j\frac{\zeta(N-j-2)}{\zeta(N-j)}.
\]
For even \(N\ge10\), the \(j=4\) ratio satisfies, using monotonicity of \(\zeta(s)\) for real \(s>1\),
\[
\frac{\lvert T_{N,6}\rvert}{\lvert T_{N,4}\rvert}
<\frac{11\pi^2}{135}\zeta(4)
=\frac{11\pi^6}{12150}<1.
\]
The last inequality follows from \(\pi<22/7\), for which the right-hand side is at most \(623589472/714717675\). For every admissible even \(j\ge6\), similarly
\[
\frac{\lvert T_{N,j+2}\rvert}{\lvert T_{N,j}\rvert}
<\frac{8\pi^2}{189}\zeta(2)
=\frac{4\pi^4}{567}<1,
\]
with rational upper bound \(937024/1361367\). Thus the magnitudes strictly decrease from \(j=4\) onward. On the other side,
\[
\frac{\lvert T_{N,4}\rvert}{\lvert T_{N,2}\rvert}
=R_2\frac{\zeta(N-4)}{\zeta(N-2)}>R_2>1,
\]
so \(j=4\) is the unique maximum for every even \(N\ge10\).

The remaining even degrees are exact. At \(N=4\), only \(j=2\) is nonzero. At \(N=6\),
\[
\frac{\lvert T_{6,4}\rvert}{\lvert T_{6,2}\rvert}=\frac{10}3>1.
\]
At \(N=8\),
\[
\frac{\lvert T_{8,4}\rvert}{\lvert T_{8,2}\rvert}=\frac73,
\qquad
\frac{\lvert T_{8,6}\rvert}{\lvert T_{8,4}\rvert}=\frac{11}9.
\]
This proves the stated modal sequence and the sharp threshold \(N_0=10\).

## Verification
The standalone checker `verify.py` uses exact rational arithmetic. It verifies the repeated-root recurrence through index \(80\), the exact small-degree ratios \(10/3\), \(7/3\), and \(11/9\), and the two rational upper bounds obtained from \(\pi<22/7\). It also independently reconstructs Bernoulli numbers and checks the unique maximizing index for every even \(N\) from \(4\) through \(40\). The finite replay is corroborative; the proof above establishes the universal statement for all even \(N\ge10\).

## Relationship to prior work
Danesh proves the trace-one recurrence identity for all \(q\), explicitly includes the repeated-root value \(q=1/4\), and records \(G_j(1/4)=j2^{1-j}\). The same paper develops a general absolute-term framework and then applies its largest-index analysis to the Fibonacci and Lucas weights, where the limiting and finite mode is \(j=8\) above a sufficient degree threshold. It does not state or derive the repeated-root modal classification above. The earlier June 2026 paper treats Fibonacci-type Bernoulli--zeta transforms but does not contain the trace-one \(q=1/4\) family.

## Limitations
The result is specific to the repeated-root parameter and the initial data \(G_0=0\), \(G_1=1\). It does not classify the modal index for arbitrary initial values in the repeated-root family or for nearby \(q\). The literature comparison is necessarily subject to the residual risk of very recent results not yet indexed. Independent audit has not been performed.

## References
1. Payam Danesh, “Cancellation profiles of Fibonacci-Lucas zeta sums,” arXiv:2609.33564v1, 27 September 2026.
2. Payam Danesh, “Bernoulli-Zeta transforms for Fibonacci-type recurrence,” DOI:10.33774/coe-2026-rxfr3, Version 1, 12 June 2026.
