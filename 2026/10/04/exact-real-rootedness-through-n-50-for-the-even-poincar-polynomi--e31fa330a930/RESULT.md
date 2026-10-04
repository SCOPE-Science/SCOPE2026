# Exact real-rootedness through \(n=50\) for the even Poincaré polynomials of \(\overline{\mathcal M}_{1,n}\)
## Finding
For every integer \(1\le n\le 50\), let
\[
P_n^{\mathrm{even}}(x)=\sum_{i=0}^n \dim H^{2i}(\overline{\mathcal M}_{1,n};\mathbf Q)x^i.
\]
Then \(P_n^{\mathrm{even}}\) is real-rooted. More precisely, \(P_1^{\mathrm{even}}=x+1\), \(P_2^{\mathrm{even}}=(x+1)^2\), and for every \(3\le n\le50\) all \(n\) roots are distinct and negative.

This gives an exact finite-range answer to Question 1.4(2) of Kiem for the entire range through \(n=50\), the large-\(n\) benchmark used in that paper's probability-distribution plot. As a consequence, Newton's inequalities give binomially normalized log-concavity, and in particular ordinary strict log-concavity, of the even Betti sequence for \(3\le n\le50\).

## Assumptions and scope
Everything is over \(\mathbf C\) with rational cohomology. The polynomials are the even-degree Poincaré polynomials of the Deligne--Mumford stacks \(\overline{\mathcal M}_{1,n}\). The computation uses exactly the even/Tate part of Kiem's formulas: the paper states that only the final cusp-form line of its formula (1.6) contributes odd cohomological degrees, so it does not enter \(P_n^{\mathrm{even}}\).

The statement is finite: it proves real-rootedness for \(1\le n\le50\), not for all \(n\). No asymptotic or inductive real-rootedness theorem is asserted.

## Proof
Kiem proves the heavy/light recursion
\[
H_{r|s}=H_{0|r+s}+\sum_{j=1}^{\min(r,r+s-2)}\sum_{k=0}^{r+s-j-2}\binom{r+s-j}{k}H_{j|k}(H_{\mathbf P^{r+s-j-k-1}}-1),
\]
and gives an explicit formula for \(H_{0|n}\). Taking its even part gives an integer polynomial recurrence. The supplied verifier implements this recurrence using only exact integer arithmetic, Stirling numbers of the second kind, and ordinary polynomial arithmetic. It first reproduces Kiem's displayed polynomials for \(1\le n\le10\).

For each \(n\), the computed polynomial is palindromic. Put \(m=\lfloor n/2\rfloor\). If \(n=2m\), palindromicity gives a unique polynomial \(Q_n(y)\in\mathbf Z[y]\) satisfying
\[
P_n^{\mathrm{even}}(x)=x^mQ_n(x+x^{-1}).
\]
If \(n=2m+1\), palindromicity and odd degree imply \(x+1\mid P_n^{\mathrm{even}}\), and after dividing by \(x+1\) one gets
\[
P_n^{\mathrm{even}}(x)=(x+1)x^mQ_n(x+x^{-1}).
\]
The verifier constructs \(Q_n\) exactly from the recurrence using \(S_0(y)=2\), \(S_1(y)=y\), and \(S_k(y)=yS_{k-1}(y)-S_{k-2}(y)\), corresponding to \(x^k+x^{-k}\).

For every \(3\le n\le50\), the certificate file supplies \(m+1\) ordered rational endpoints
\[
b_0<b_1<\cdots<b_m=-2
\]
with exact nonzero values \(Q_n(b_i)\) of alternating sign. Hence the intermediate value theorem gives at least one real root in every interval \((b_{i-1},b_i)\). Since \(\deg Q_n=m\), these are all its roots and each is simple. Every interval lies in \(( -\infty,-2)\), so every root \(y\) of \(Q_n\) satisfies \(y<-2\).

For such \(y\), the equation \(x+x^{-1}=y\) is equivalent to \(x^2-yx+1=0\), whose two roots are distinct negative reals. Thus each of the \(m\) roots of \(Q_n\) yields two distinct negative reciprocal roots of \(P_n^{\mathrm{even}}\); when \(n\) is odd there is in addition the root \(x=-1\). This accounts for the full degree \(n\), proving the claim.

## Verification
Run `python3 artifacts/verify.py`. The script uses only the Python standard library. It:

1. recomputes Kiem's even/Tate recurrence for every \(1\le n\le50\);
2. checks the displayed \(n\le10\) values from the source;
3. checks positivity, degree and palindromicity;
4. reconstructs every \(Q_n\) and compares it byte-for-byte as integer coefficient data with `artifacts/root_brackets.json`;
5. evaluates all rational bracket endpoints exactly with `fractions.Fraction` and checks strict sign alternation;
6. checks that all bracket intervals lie to the left of \(-2\).

A successful replay ends with `VERIFY_OK`. The saved output is in `artifacts/verification_output.txt`.

## Relationship to prior work
Kiem's September 11, 2026 preprint gives the recursion used here and explicitly asks whether the even-degree Poincaré polynomial of \(\overline{\mathcal M}_{1,n}\) is real-rooted. The paper notes that previous explicit computations were available through \(n=20\), displays formulas through \(n=10\), and uses \(n=50\) as its large finite benchmark for the Betti distribution. It does not report a real-rootedness verification through \(n=50\).

Bérczi--Kiem prove real-rootedness for \(\overline{\mathcal M}_{0,n}\), not genus one, using a bivariate deformation and an interlacing argument. That theorem neither implies nor contains the genus-one finite-range statement proved here.

Targeted searches for the genus-one statement and the \(n=50\) benchmark found no published record covering this claim. The closest records concerned unrelated real-rooted polynomial families or genus-one enumerative problems.

## Limitations
The result is an exact finite computation and does not establish real-rootedness for \(n>50\). The certificate proves existence and uniqueness of one \(Q_n\)-root per rational interval but does not provide closed forms for the roots. It also does not prove the conjectural asymptotic Gaussian law or any specific definition of \(k\)-ultra log-concavity beyond the standard Newton inequalities implied by real-rootedness.

## References
1. Young-Hoon Kiem, *Hodge-Deligne and Poincaré polynomials of \(\overline{\mathcal M}_{1,n}\)*, arXiv:2609.12507v1, 11 September 2026. https://arxiv.org/abs/2609.12507
2. Gergely Bérczi and Young-Hoon Kiem, *Real-rootedness of the Poincaré polynomials of \(\overline{\mathcal M}_{0,n}\): an AI-assisted proof*, arXiv:2605.29151, 2026. https://arxiv.org/abs/2605.29151
