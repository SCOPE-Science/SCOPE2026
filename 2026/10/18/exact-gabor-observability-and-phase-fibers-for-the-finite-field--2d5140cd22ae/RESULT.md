# Exact Gabor observability and phase fibers for the finite-field hyperbola

## Finding
Fix any odd prime power \(q\ge3\), let \(F=\mathbb F_q\), \(G=F^2\), and define the **multiplicative hyperbola** and its indicator window by
\[
H=\{(t,t^{-1}):t\in F^\times\},\qquad g=\mathbf1_H.
\]
Let \(\chi\) be the quadratic character on \(F\), extended by \(\chi(0)=0\). For \(D=H-H\) the complete overlap, self-ambiguity, and Gabor-observability classification is
\[
\boxed{D=\{(0,0)\}\cup\{(a,b)\in(F^\times)^2:\chi(1-4/(ab))\in\{0,1\}\},\quad |D|=1+\frac{(q-1)^2}{2}.}
\]
For every displacement \(h\in G\) and every modulation \(\xi\in G\), the self-ambiguity coefficient \(A_g(h,\xi)\) is nonzero **if and only if** \(h\in D\). Consequently the complex linear lifting of all Gabor intensity measurements has rank
\[
\boxed{\operatorname{rank}_{\mathbb C}\mathcal L_g=q^2\left(1+\frac{(q-1)^2}{2}\right),\qquad \operatorname{nullity}_{\mathbb C}\mathcal L_g=q^4-\operatorname{rank}_{\mathbb C}\mathcal L_g.}
\]
More strongly, for every **nonzero** signal \(f:G\to\mathbb C\), let \(S=\operatorname{supp}f\), and join distinct \(x,y\in S\) whenever \(x-y\in D\). If this graph has \(c\) connected components, the complete fiber of the full spectrogram \(|V_gf|\) consists of the signals obtained by multiplying \(f\) by independent unimodular constants on those components; after quotienting by global phase the fiber is \((\mathbb S^1)^{c-1}\).

The full-support graph is connected **if and only if** \(q\ge5\). At \(q=3\) it has exactly three components, and its full-support fiber has two independent relative phases. In contrast, for every \(q\) the indicator window does not perform phase retrieval on *all* signals: a nonzero horizontal displacement is outside \(D\), so signals supported on two corresponding sites have an undetermined relative phase.

## Assumptions and scope
All finite fields are of odd characteristic \(p\) with \(q=p^e\), with no assumption that \(q\) is prime. Let \(\operatorname{Tr}:F\to\mathbb F_p\) be the absolute trace, and use characters \(\psi_\xi(x)=\exp(2\pi i\operatorname{Tr}(\xi\cdot x)/p)\), with \(\xi\cdot x=\xi_1x_1+\xi_2x_2\). The STFT is
\[
V_gf(u,\xi)=\sum_{x\in G} f(x)\overline{g(x-u)}\,\overline{\psi_\xi(x)}.
\]
The self-ambiguity coefficient is \(A_g(h,\xi)=\sum_{z\in G}g(z)\overline{g(z-h)}\psi_\xi(z)\). The lifted map acts on **all complex** \(q^2\times q^2\) matrices, not merely Hermitian matrices or rank-one projectors:
\[
\mathcal L_g(X)_{u,\xi}=\operatorname{tr}\bigl(X\,|M_\xi T_ug\rangle\langle M_\xi T_ug|\bigr).
\]
Positive rescaling of \(g\) changes measurement values but not rank, kernel, or phase fibers. Graph components count only the nonzero signal support. No result is asserted for even characteristic or for a different geometric window.

## Proof
**1. Hyperbola-overlap arithmetic.** Write \(h=(a,b)\). If \((t,t^{-1})-(s,s^{-1})=(a,b)\) with \(t,s\ne0\), then either \(h=0\) and \(t=s\), or \(a=t-s\ne0\) and \(b=-a/(st)\ne0\). In the latter case \(s=t-a\), so \(t\) must solve
\[
t^2-at+a/b=0,
\]
with discriminant \(a^2(1-4/(ab))\). Both roots, whenever they exist, are automatically nonzero and distinct from \(a\). Thus the overlap size \(m(h)=|H\cap(H+h)|\) is \(q-1\) at \(h=0\), and for \(ab\ne0\) is \(1+\chi(1-4/(ab))\); otherwise it is zero. The indicator at each fixed nonzero product \(ab=z\) occurs at exactly \(q-1\) pairs \((a,b)\). The bijection \(z\mapsto 1-4/z\) maps \(F^\times\) onto \(F\setminus\{1\}\). Exactly \((q-3)/2\) values of \(z\) give a nonzero square discriminant, and one value gives discriminant zero. Equivalently, count ordered pairs \(t\ne s\): precisely \((q-1)(q-2)\) differences, among which \(q-1\) have multiplicity one (discriminant zero, when \(t=-s\)) and the others multiplicity two; hence \(|D|=1+(q-1)+[(q-1)(q-2)-(q-1)]/2=1+(q-1)^2/2\).

**2. Cyclotomic no-cancellation.** For \(h\in D\), the coefficient \(A_g(h,\xi)\) is a sum of \(m(h)\in\{1,2,q-1\}\) complex \(p\)-th roots of unity. If such a sum vanished, its nonnegative integer residue multiplicities would be all equal by irreducibility of \(1+X+\cdots+X^{p-1}\) over \(\mathbb Q\). It would follow that \(p\mid m(h)\), impossible because \(p\) is odd and \(p\nmid q-1\). For \(h\notin D\), the overlap is empty, so every coefficient vanishes. This proves the all-frequency ambiguity-zero classification without any approximate character-sum estimate.

**3. Exact lifted rank and matrix kernel.** For each lag \(h\), the inverse Fourier transform in modulation of the STFT intensity yields, up to a fixed harmless sign convention,
\[
C_h(u)=\sum_{x\in G}f(x)\overline{f(x-h)}\,g(x-u)g(x-h-u).
\]
For an arbitrary matrix \(X\), the identical linear identity holds with \(f(x)\overline{f(x-h)}\) replaced by \(X_{x,x-h}\). Fourier transforming \(C_h\) in \(u\) gives an invertible Fourier transform of the lag diagonal, multiplied by the Fourier transform of \(z\mapsto g(z)g(z-h)\). That multiplier is, up to conjugation/reversal, \(A_g(h,\xi)\). Step 2 shows that **every** entry on a lag \(h\in D\) is individually recoverable, whereas for \(h\notin D\) none affects any measurement. The different lag diagonals form a direct sum; each has \(|G|=q^2\) entries. Thus rank equals \(q^2|D|\), and the kernel is exactly
\[
\boxed{\ker\mathcal L_g=\{X:X_{x,y}=0\ \text{whenever }x-y\in D\}.}
\]

**4. Complete phase fibers.** At lag zero, Step 3 recovers \(f(x)\overline{f(x)}=|f(x)|^2\) for every \(x\), so the support and the modulus of each nonzero coordinate are fixed. At every lag \(h\in D\setminus\{0\}\), the recovered products \(f(x)\overline{f(x-h)}\) force the relative phases on every edge of the stated support graph. Consequently two signals have identical data precisely when their nonzero coordinates differ by one common phase per connected component. Conversely these independent component phases preserve every product on every observed lag, and Step 3 proves that no other information is measured. This also proves the phase-torus dimension.

**5. Sharp full-support transition.** When \(q=3\), \(H=\{(1,1),(-1,-1)\}\), so \(D=\{(t,t):t\in\mathbb F_3\}\). Its Cayley graph on \(G\) consists of three additive cosets. For \(q\ge5\), fix arbitrary \(a\in F^\times\). Among the \(q-2\ge3\) values \(t\in F\setminus\{0,a\}\), the quadratic expression \(t(t-a)\) attains at least two distinct values (each fiber has at most two elements). Hence \(D\) contains two elements \((a,b_1),(a,b_2)\) with \(b_1\ne b_2\), and the additive subgroup generated by \(D\) contains \((0,b_1-b_2)\ne0\). Every dilation \((x,y)\mapsto(\lambda x,\lambda^{-1}y)\), \(\lambda\in F^\times\), preserves \(H\), hence preserves \(D\) and its generated subgroup. Therefore this subgroup contains the entire vertical axis. It also contains, for each \(a\ne0\), at least one \((a,b)\in D\); subtracting the appropriate vertical vector gives \((a,0)\). It is therefore all of \(G\), proving connectivity. Since \((1,0)\notin D\), two-point counterexamples to unrestricted phase retrieval exist for every \(q\).

## Verification
Execute `python3 checks/verify.py` using only the Python standard library. For the seven fields of orders \(3,5,7,9,11,13,25\), the program independently constructs \(H\), computes every difference and translates-overlap, checks the discriminant characterization and counts, evaluates **every** displacement-modulation ambiguity coefficient by exact cyclotomic residue counts, and computes all connected components of the full-support graph. It checks that rank equals the number of nonzero ambiguity coefficients, including extension fields \(\mathbb F_9\) and \(\mathbb F_{25}\). A separate direct complex lifting-matrix rank calculation at \(q=3\) yielded \(27\) as predicted; it is a numerical cross-check, while the cyclotomic checker uses no floating tolerance. Finite verifications supplement, but do not establish, the universal proof.

## Relationship to prior work
Alaifari–Wellershoff [1] develop finite-dimensional Gabor ambiguity reconstruction and support-component stability; Bartusel [2, Theorem 2.2.3] proves a general connected-component phase-fiber criterion under full modulation nonvanishing for cyclic groups. **The component-phase logic here is previously known**, and the present result extends that argument to the specific noncyclic groups \(\mathbb F_q^2\), with the missing explicit hyperbola-window noncancellation, computed operator kernel, and sharp field-order transition.

Iosevich–Murphy–Pakianathan [3] study Fourier decay and Kloosterman sums of the same multiplicative hyperbola. Previously published exact fourth-moment studies of this hyperbola [4,5] already encode the exceptional pair-sum collisions, and by central symmetry \(H=-H\) they imply its unweighted difference multiplicities; **the support-count formula alone is not claimed original here**. Their results do not state all self-ambiguity frequencies, the complete lifted Gabor kernel, or phase-retrieval fiber classification. A related published Gabor tomography theorem [6] treats hyperbolic shells \(x\cdot y=1\) only in ambient dimension at least four; its nonisotropic sections and frequency-dependent zero mechanism differ from this dimension-two result. Searches for Gabor phase retrieval under inverse-graph, multiplicative-conic, and Kloosterman-window terminology did not locate an exact covering theorem.

## Limitations
The result assumes every time-frequency shift/modulation is measured and the window is exactly an unweighted hyperbola indicator over an odd-order finite field. It does not give stable reconstruction constants, classify incomplete measurements, extend to even characteristic or general rings, or show global pure-state phase retrieval on all sparse signals. The general graph propagation is known prior theory; the mathematical contribution claimed is the specific field-uniform arithmetic and its quantitative recovery consequences. An older differently indexed equivalent calculation remains a novelty risk.

## References
1. R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296v1 (12 January 2019), https://arxiv.org/abs/1901.05296.
2. D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on Z, Z_d and R^d*, arXiv:2206.06729v1 (14 June 2022), https://arxiv.org/abs/2206.06729; J. Fourier Anal. Appl. 29 (2023), article 53, Theorem 2.2.3.
3. A. Iosevich, B. Murphy, and J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657v1 (29 May 2014), https://arxiv.org/abs/1405.7657.
4. *Sharp fourth-moment extension on the finite-field multiplicative hyperbola* (public research result), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-fourth-moment-extension-on-the-finite-field-multiplicative--0835fe791166.
5. *Sharp fourth-moment extension and global deficit identity on the split finite-field hyperbola* (public research result), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-global-deficit-identity-on-the--1c3c2c761f07.
6. *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields* (public research result), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-gabor-tomography-rank-for-hyperbolic-quadratic-shells-over--b9e240edb677.
