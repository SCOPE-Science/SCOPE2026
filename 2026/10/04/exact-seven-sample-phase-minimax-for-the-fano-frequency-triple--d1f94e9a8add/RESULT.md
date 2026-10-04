# Exact seven-sample phase minimax for the Fano frequency triple
## Finding
Let \(\zeta=e^{2\pi i/7}\). For \(|u|=|v|=1\), put
\[
P_{u,v}(k)=1+u\zeta^k+v\zeta^{3k},\qquad k\in\mathbb Z_7.
\]
Then
\[
\min_{|u|=|v|=1}\max_{k\in\mathbb Z_7}|P_{u,v}(k)|^2=\frac{7+\sqrt{21}}2.
\]
One minimizer is
\[
u=e^{4\pi i/3},\qquad v=e^{2\pi i/3}.
\]
For this pair the seven squared moduli are exactly one copy of \(0\), three copies of
\[
A=\frac{7+\sqrt{21}}2,
\]
and three copies of
\[
B=\frac{7-\sqrt{21}}2.
\]

## Assumptions and scope
The optimization is only over the two coefficient phases: all three Fourier coefficients have modulus \(1\), the frequency set is \(\{0,1,3\}\subset\mathbb Z_7\), and the objective is the maximum over the seven characters of \(\mathbb Z_7\). This is a sampled, finite-cyclic version of the prescribed-modulus phase minimax problem for trigonometric trinomials. It is not the continuous-circle maximum-modulus problem and it is not the Sidon constant, where coefficient magnitudes are also optimized.

## Proof
For fixed \(u,v\), write
\[
q_k=|P_{u,v}(k)|^2,
\qquad
m_j=\frac17\sum_{k=0}^6 q_k^j.
\]
Root-of-unity orthogonality gives
\[
m_1=3,\qquad m_2=15.
\]
A direct Laurent expansion gives
\[
m_3=93+3\left(X+X^{-1}+Y+Y^{-1}+XY+(XY)^{-1}\right),
\]
where
\[
X=u^2v^{-3},\qquad Y=uv^2.
\]
Since \(|X|=|Y|=1\),
\[
3+X+X^{-1}+Y+Y^{-1}+XY+(XY)^{-1}
=|1+X+Y^{-1}|^2\ge0.
\]
Hence
\[
m_3\ge84.
\]
The fourth moment has the exact expansion
\[
m_4=639+52\left(X+X^{-1}+Y+Y^{-1}+XY+(XY)^{-1}\right),
\]
so
\[
m_4=\frac{52}{3}m_3-973.
\]

Set
\[
A=\frac{7+\sqrt{21}}2,
\qquad
B=\frac{7-\sqrt{21}}2.
\]
Thus \(A+B=7\) and \(AB=7\). Suppose \(q_k\le A\) for every \(k\). On \([0,A]\), the polynomial
\[
h(x)=x(A-x)(x-B)^2
\]
is nonnegative. Using the formulas for \(m_1,m_2,m_3,m_4\), its sample average is
\[
\frac17\sum_{k=0}^6 h(q_k)
=-\frac{41+3\sqrt{21}}6\,(m_3-84)\le0.
\]
Nonnegativity of every summand therefore forces equality throughout. In particular, if the maximum were strictly smaller than \(A\), every \(q_k\) would lie in \(\{0,B\}\), which is impossible because their average is \(m_1=3>B\). Hence
\[
\max_k q_k\ge A
\]
for every unimodular \(u,v\).

It remains to attain the bound. Let \(\omega=e^{2\pi i/3}\) and choose \(u=\omega^2\), \(v=\omega\). Then \(P_{u,v}(0)=1+\omega+\omega^2=0\). For a nontrivial seventh root \(t\), the difference between the expressions for \(q(t^2)\) and \(q(t)\) has real part
\[
\operatorname{Re}\!\left(\omega^2(t^4-t)+\omega(t^6-t^3)\right)=0,
\]
because complex conjugation sends the quantity inside the real part to its negative, using \(t^7=1\). Thus the six nonzero samples split into the two doubling orbits \(\{1,2,4\}\) and \(\{3,5,6\}\), with one common squared modulus on each orbit. Call them \(a\) and \(b\). Since \(q_0=0\), the already proved identities \(m_1=3\) and \(m_2=15\) yield
\[
a+b=7,\qquad a^2+b^2=35,
\]
so \(ab=7\). Therefore \(a,b\) are the roots of \(x^2-7x+7\), namely \(A\) and \(B\). The maximum is exactly \(A\), proving the claim.

## Verification
The accompanying checker expands the first four sampled moments in the Laurent group algebra exactly over the rational numbers, verifies \(m_1=3\), \(m_2=15\), the factored nonnegative expression for \(m_3-84\), and the identity \(m_4=(52/3)m_3-973\). It also checks the coefficient identity for the polynomial certificate \(h\) and numerically confirms the stated seven-value extremizer to high precision. Running `python3 artifacts/verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Neuwirth's prescribed-modulus trigonometric-trinomial problem studies the maximum over the entire circle and proves a general continuous phase-minimization theorem; the present objective instead takes a maximum over only the seven characters of a finite cyclic group. The continuous theorem therefore does not imply this sampled minimax value, and its minimizing phase mechanism is different. Strohmer and Heath construct harmonic Grassmannian frames from cyclic difference sets, including the \(7\)-vector, \(3\)-dimensional complex setting, but their objective is maximal pairwise frame correlation, not the phase-only peak of a linear combination of the frame rows. Graham's finite-group Sidon work notes that \(\{0,1,2\}\) and \(\{0,1,3\}\) form the two equivalence classes of three-element subsets of \(\mathbb Z_7\) and have different Sidon constants; that norm extremal problem allows coefficient magnitudes to vary and does not state the fixed-unimodular minimax above.

## Limitations
Only the specific seven-point frequency triple \(\{0,1,3\}\) is evaluated. No classification of all minimizer phases is claimed. The literature comparison found no statement of this exact sampled phase-only constant, but terminology varies across harmonic-frame, sequence-design, crest-factor, and finite Fourier literatures, so unindexed prior appearance remains a residual risk.

## References
1. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first public 2007-03-08; later J. Anal. Math. 104 (2008), 371–396.
2. T. Strohmer and R. W. Heath Jr., *Grassmannian Frames with Applications to Coding and Communication*, Appl. Comput. Harmon. Anal. 14 (2003), 257–275.
3. C. C. Graham, *A beastiary of sets having extremal Sidon constant, or, there must be more than one theorem somewhere here*, arXiv:1910.00924v1 (2019).
