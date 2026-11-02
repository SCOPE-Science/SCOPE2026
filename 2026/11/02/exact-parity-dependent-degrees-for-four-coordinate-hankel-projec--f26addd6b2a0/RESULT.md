# Exact parity-dependent degrees for four-coordinate Hankel projections

## Finding

For each integer \(n\ge6\), consider the rank-at-most-two Hankel determinantal variety \(H_{2,n}\subset\mathbb A^n_{\mathbb C}\). Its coordinate map retaining the first, third, fifth, and last coordinates,
\[
\pi_{\{1,3,5,n\}}:H_{2,n}\longrightarrow\mathbb A^4,
\]
is dominant and generically finite, with degree
\[
\boxed{\deg\pi_{\{1,3,5,n\}}=4\left\lfloor\frac{n-4}{2}\right\rfloor
=\begin{cases}2n-8,&n\text{ even},\\2n-10,&n\text{ odd}.\end{cases}}
\]
Its values at \(n=7,8,9,10,11,12\) are, respectively, \(4,8,8,12,12,16\), agreeing with a previously published finite table; the result here is the all-\(n\) formula and proof.

## Assumptions and scope

The ground field is \(\mathbb C\). The variety \(H_{2,n}\) is defined by all \(3\times3\) minors of the \(3\times(n-2)\) Hankel matrix whose entry in row \(i\) and column \(j\) is \(x_{i+j-1}\). Its dimension is \(4\); generic points admit unique unordered two-node presentations
\[
x_{j+1}=A u^j+B v^j\quad(0\le j<n),
\]
with \(u\ne v\), \(AB\ne0\), and nonzero leading Hankel minor. The presentation follows by the standard recurrence and is birational after exchanging the two node-weight pairs. Fix generic values \(x_1=s_0\), \(x_3=s_2\), \(x_5=s_4\) satisfying \(s_0s_2\Delta\ne0\), where \(\Delta=s_2^2-s_0s_4\). The genericity conditions exclude only proper algebraic subsets and therefore do not alter the generic projection degree.

## Proof

**1. Birational conic for the first three selected observations.** Write \(m_j=x_{j+1}\), \(S=u+v\), \(P=uv\). The two-node recurrence is \(m_{j+2}=S m_{j+1}-P m_j\). From \(m_0=s_0\), \(m_2=s_2\) we get
\[
m_1=\frac{s_2+s_0P}{S}.
\]
Since \(m_4=(S^2-2P)s_2-P^2s_0=s_4\), the remaining parameters satisfy
\[
C:\quad S^2=Q(P),\qquad Q(P)=\frac{s_0P^2+2s_2P+s_4}{s_2}.
\]
For \(s_0s_2\Delta\ne0\), its smooth projective completion is a nonsingular conic. Conversely, for a generic point \((S,P)\in C\) with \(S\ne0\), two distinct roots \(u,v\) of \(t^2-St+P\) and the linear equations \(A+B=s_0\), \(Au+Bv=m_1\) uniquely produce an unordered two-node presentation. This proves birationality of the generic three-observation fiber and \(C\). In particular \(\mathbb C(H_{2,n})\) restricted to the three-observation fiber is \(\mathbb C(C)\) and the final observation becomes the rational function \(m_{n-1}\) on \(C\).

**2. Degree growth of even and odd moments.** The recurrence and \(S^2=Q(P)\) give polynomials \(E_{2k}(P)\), \(N_{2k+1}(P)\) such that \(m_{2k}=E_{2k}(P)\) and \(m_{2k+1}=N_{2k+1}(P)/S\). Base cases are
\[
E_2=s_2,\quad E_4=s_4,\quad N_3=s_2P+s_4,
\]
\[
N_5=-\frac{\Delta}{s_2}P^2+s_4P+\frac{s_4^2}{s_2},\qquad
E_6=-\frac{\Delta}{s_2}P^2+\frac{s_4^2}{s_2}.
\]
For all \(k\ge2\), the recurrence reduces to
\[
N_{2k+1}=Q(P)E_{2k}-P N_{2k-1},\qquad
E_{2k+2}=N_{2k+1}-P E_{2k}.
\]
The base equations and induction using the leading term of \(Q\) prove
\[
\deg_P E_{2k}=2k-4\quad(k\ge3),\qquad
\deg_P N_{2k+1}=2k-2\quad(k\ge2).
\]
Indeed both relevant leading coefficients are nonzero: for \(E_{2k}\), it is \(-\Delta s_0^{k-3}/s_2^{k-2}\); for \(N_{2k+1}\), it is \(-\Delta s_0^{k-2}/s_2^{k-1}\). The case \(k=2\) for \(N_5\) and the case \(k=3\) for \(E_6\) are the displayed base formulas; at all subsequent steps, the term \(Q E\) has strictly higher degree than the subtracted \(P N\), and \(N\) higher than the subtracted \(P E\).

**3. Exact map degree for an even last moment.** If \(n-1=2k\ge6\), then \(m_{n-1}=E_{2k}(P)\), of degree \(2k-4=n-5\) as a polynomial in \(P\). The function \(P:C\to\mathbb P^1\) has degree two (two square roots \(S=\pm\sqrt{Q(P)}\) generically). Therefore the composition has degree \(2(2k-4)=2n-10\).

**4. Exact map degree for an odd last moment.** If \(n-1=2k+1\ge5\), write \(m_{n-1}=N_{2k+1}(P)/S\). For a generic target value \(z\ne0\), eliminate \(S\) between \(zS=N_{2k+1}(P)\) and \(S^2=Q(P)\) to obtain
\[
N_{2k+1}(P)^2-z^2Q(P)=0.
\]
Its degree in \(P\) is exactly \(2(2k-2)=2n-8\), since \(\deg N_{2k+1}\ge2>\deg Q/2\). Each generic root determines exactly one \(S=N_{2k+1}(P)/z\). The generic roots are simple because the resulting nonconstant rational map is separable in characteristic zero; they avoid the finitely many excluded loci. Thus the map has degree \(2n-8\), completing the proof.

## Verification

The self-contained `verify_degree.py` implements the exact recurrence in the quotient \(\mathbb Q[P,S,S^{-1}]/(S^2-Q(P))\), specialized at \((s_0,s_2,s_4)=(2,3,5)\), for \(6\le n\le21\). It checks the parity-specific polynomial degrees, the odd elimination polynomials, and the six degree values from the published table. Running `python verify_degree.py` prints `VERIFY_OK`. This is a finite consistency check; the uniform theorem is proved algebraically above, independently of these tests.

## Relationship to prior work

E. Reed and M. C. Tsakiris, *On Hankel Determinantal Matroids* (arXiv:2610.27554v1, October 20, 2026), establish generic finiteness of Hankel coordinate projections and degree upper bounds. Section 5.1, Remark 6, explicitly lists degrees for the six instances \(\{1,3,5,n\}\) with \(7\le n\le12\), without an all-\(n\) theorem for this pattern; Section 5.3 treats three consecutive selected coordinates, which the current pattern lacks. The present formula extends this tabulation to every \(n\ge6\) and explains its parity behavior via the conic geometry.

D. Batenkov, *Decimated generalized Prony systems* (arXiv:1308.0753v1, 2013), treats equally spaced moments and their node-root ambiguities. Those arguments motivate the recurrence viewpoint, but the non-equally-spaced four-observation pattern \(\{1,3,5,n\}\), its degree, and its parity formula are not results of the inspected material. Classical algebraic secant-variety degree formulas count a different invariant from coordinate-projection degrees. No definitive global priority claim is made.

## Limitations

This is a characteristic-zero, rank-two result for precisely the specified four-coordinate pattern. It does not compute branch divisors, exceptional fibers, monodromy, arbitrary sparse patterns, or scheme-theoretic multiplicities of non-generic completions. The conic parametrization is birational only on the indicated generic open locus. Although substantial source text and targeted searches were inspected, an unlocated equivalent sparse-Prony or projection-degree formula remains a literature-priority risk. Independent mathematical validation has not been performed.

## References

- E. Reed and M. C. Tsakiris, *On Hankel Determinantal Matroids*, arXiv:2610.27554v1 (first submitted October 20, 2026), particularly Sections 2, 4, 5.1 and 5.3. https://arxiv.org/html/2610.27554v1
- D. Batenkov, *Decimated generalized Prony systems*, arXiv:1308.0753v1 (2013), especially the decimation analysis and Section 4. https://arxiv.org/html/1308.0753v1
