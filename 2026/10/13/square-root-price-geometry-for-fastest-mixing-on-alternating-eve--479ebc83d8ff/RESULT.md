# Square-root price geometry for fastest mixing on alternating even cycles

## Finding
For every integer \(m\ge2\) and every pair of positive prices \(c,d\), consider the even cycle \(C_{2m}\) with alternating edge prices \(c,d\). Among **all individual, nonnegative conductance allocations** with unit total price, the continuous-time symmetric Markov generator has a uniquely maximal spectral gap. Put
\[
\alpha=\frac{\pi}{m},\quad r=\cos\alpha,\quad D=c+d+2r\sqrt{cd}.
\]
Its unique optimal edge conductances alternate between
\[
\boxed{a^*=\frac{1+r\sqrt{d/c}}{mD},\qquad b^*=\frac{1+r\sqrt{c/d}}{mD}},
\]
with \(a^*\) on price-\(c\) edges and \(b^*\) on price-\(d\) edges. The exact optimal gap is
\[
\boxed{\gamma^*=\frac{2\sin^2\alpha}{mD}}.
\]
All optimal edges are strictly positive, and the optimal Fiedler eigenspace has real dimension two. In the large-ring limit with fixed prices,
\[
\frac{a^*}{b^*}\longrightarrow\sqrt{\frac dc},\qquad
m^3\gamma^*\longrightarrow\frac{2\pi^2}{(\sqrt c+\sqrt d)^2}.
\]
For the four-cycle \(m=2\), the two optimal conductances are equal regardless of the price ratio. Thus the finite-size price response interpolates exactly between equal per-edge investment at four vertices and inverse-square-root pricing on large rings.

## Assumptions and scope
Label vertices \(0,1,\ldots,2m-1\) modulo \(2m\). Edge \(\{2k,2k+1\}\) has price \(c>0\) and conductance \(w_{2k}\ge0\); edge \(\{2k+1,2k+2\}\) has price \(d>0\) and conductance \(w_{2k+1}\ge0\), for \(0\le k<m\). The budget constraint is
\[
\sum_{k=0}^{m-1}(cw_{2k}+dw_{2k+1})=1.
\]
The real symmetric Laplacian is \(L(w)=\sum_{j=0}^{2m-1}w_j(e_j-e_{j+1})(e_j-e_{j+1})^{\mathsf T}\), using indices modulo \(2m\). The Markov generator is \(-L(w)\); its invariant measure is uniform when connected. The objective \(\gamma(w)=\lambda_2(L(w))\) is the second-smallest Laplacian eigenvalue, **not** discrete-time second-largest eigenvalue modulus, effective resistance, or a nonreversible mixing rate. Zero conductances are allowed during optimization; uniqueness and positive conductances are conclusions.

## Proof
**1. A dual circle certificate.** Let \(s=\sqrt c\), \(t=\sqrt d\), \(\theta=2\alpha\), and \(D=s^2+t^2+2st\cos\alpha\). There is a unique \(u\in(0,\alpha)\) such that
\[
\sin u=\frac{s\sin\alpha}{\sqrt D},\qquad
\sin(\alpha-u)=\frac{t\sin\alpha}{\sqrt D}.
\]
Indeed one may set \(u=\arg(t+s e^{i\alpha})\), whose argument lies strictly between \(0\) and \(\alpha\), then use the sine rule. Define \(z\in\mathbb C^{2m}\) by
\[
z_{2k}=e^{2ik\alpha},\qquad z_{2k+1}=e^{i(2k\alpha+2u)}.
\]
Since \(m\ge2\), the geometric sum vanishes: \(\sum_j z_j=0\). Also \(\sum_j|z_j|^2=2m\). The two successive chord lengths satisfy
\[
|z_{2k}-z_{2k+1}|^2=\frac{4c\sin^2\alpha}{D},\qquad
|z_{2k+1}-z_{2k+2}|^2=\frac{4d\sin^2\alpha}{D}.
\]
Consequently, every feasible allocation obeys the **global**, not merely symmetry-restricted, Rayleigh bound
\[
\lambda_2(L(w))\le\frac{z^*L(w)z}{z^*z}
=\frac{4\sin^2\alpha}{2mD}\sum_k(cw_{2k}+dw_{2k+1})
=\frac{2\sin^2\alpha}{mD}=:\Gamma.
\]
The inequality is valid for complex \(z\perp\boldsymbol 1\) because the real symmetric Rayleigh principle extends to complex vectors.

**2. Attainment with explicit conductances.** Define
\[
a=\frac{1+r(t/s)}{mD},\qquad b=\frac{1+r(s/t)}{mD}.
\]
Both are positive and \(m(ca+db)=1\). The elementary identities
\[
\sin(2u)=\frac{2s\sin\alpha(t+sr)}D,\quad
\sin(2\alpha-2u)=\frac{2t\sin\alpha(s+tr)}D
\]
imply \(a\sin(2u)=b\sin(2\alpha-2u)\). Hence the imaginary part of \(L(a,b)z/z_j\) vanishes at both vertex parities. Its common real part equals
\[
a(1-\cos2u)+b(1-\cos(2\alpha-2u))
=\frac{2\sin^2\alpha}{D}(ca+db)=\Gamma.
\]
Thus \(L(a,b)z=\Gamma z\). To confirm that this is the smallest positive eigenvalue, use the two-vertex Bloch decomposition for \(k=0,\ldots,m-1\), which gives
\[
\lambda_k^{\pm}=a+b\pm\sqrt{a^2+b^2+2ab\cos(2\pi k/m)}.
\]
The zero mode is \(\lambda_0^-=0\), its companion is \(2(a+b)\), and the smallest of all remaining branches is \(\lambda_1^-\) (also \(\lambda_{m-1}^-\)). Since \(z\) is the lower-branch Bloch mode at \(k=1\), its eigenvalue is \(\lambda_1^-=\Gamma\). For \(m=2\), the off-diagonal Bloch block vanishes at the candidate \(a=b\) and both modes at \(k=1\) equal \(\Gamma=2a\). This proves \(\gamma(a,b)=\Gamma\) and hence global optimality. The gap has real multiplicity two, including the four-cycle.

**3. Uniqueness without assuming symmetric allocations.** Let \(\widetilde w\) be any globally optimal feasible allocation. The same fixed test vector \(z\) has Rayleigh quotient \(\Gamma\) for every feasible allocation. Since \(\lambda_2(L(\widetilde w))=\Gamma\), equality in the Rayleigh principle implies \(L(\widetilde w)z=\Gamma z\). Subtract the attained equation for \(w^*\) and let \(h_j=\widetilde w_j-w_j^*\in\mathbb R\). At each vertex \(j\),
\[
h_{j-1}(z_j-z_{j-1})+h_j(z_j-z_{j+1})=0.
\]
The three neighboring values \(z_{j-1},z_j,z_{j+1}\) are **distinct points on the unit circle**: their two successive positive arguments are \(2u\) and \(2(\alpha-u)\), and their total is at most \(\pi\). Three distinct points of a circle cannot be collinear. Therefore these two complex chord differences are linearly independent over \(\mathbb R\), forcing \(h_{j-1}=h_j=0\). This holds at every vertex, so \(\widetilde w=w^*\).

**4. Large rings and a concrete instance.** As \(m\to\infty\), \(\cos(\pi/m)\to1\), \(\sin(\pi/m)\sim\pi/m\), and \(D\to(\sqrt c+\sqrt d)^2\). Substituting into the exact formulas gives the stated limits and, individually,
\[
ma^*\to\frac{1}{\sqrt c(\sqrt c+\sqrt d)},\qquad
mb^*\to\frac{1}{\sqrt d(\sqrt c+\sqrt d)}.
\]
For \(m=3,c=1,d=4\), the exact optimizer is \(a^*=2/21\), \(b^*=5/84\), and \(\gamma^*=1/14\); its weighted budget is \(3(a^*+4b^*)=1\). All these values follow by substituting \(\cos(\pi/3)=1/2\).

## Verification
The accompanying `verify.py` checks the exact rational six-cycle instance, the explicit Laplacian spectra, the complex eigenvector and edge-chord equalities for 75 parameter instances, and 600 randomized **nonsymmetric** feasible allocations. It uses Python 3 and NumPy (`python3 verify.py`). These finite checks are not the proof of the universal statement; the preceding Rayleigh certificate and chord-independence argument supply that proof.

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis (2006), Section 5.3 (pp. 696–697), derive the **uniform-cost cycle** optimum and state that arbitrary cycle costs are more complicated, proving a two-dimensional dual-configuration result rather than this alternating-price allocation. The present cost-normalized formulas and the global uniqueness assertion therefore do not follow as stated from their published cycle theorem, although their duality framework motivates the circle-certificate method. Boyd, Diaconis, Parrilo, and Xiao (2009) analyze **discrete-time** fastest mixing with symmetries, including unweighted cycles; their SLEM objective and normalization differ. Gerencsér, Hendrickx, and Van Dooren (2015) analyze uniform-cycle **discrete-time** spectral gaps and perturbations, not the continuous-time alternating-price global optimum here. This finding is a structured exact specialization of the established eigenvalue-optimization framework, not a claim to invent that framework.

## Limitations
The result assumes an even ring, exactly two alternating positive edge prices, symmetric continuous-time rates, and a total *linear conductance-price* budget. It does not classify arbitrary independent prices on every edge, odd cycles, nonuniform stationary masses, discrete-time fastest mixing by eigenvalue modulus, nonreversible chains, or other graph topologies. A logically equivalent older closed-form specialization may exist in literature not identified by the searches reported in the accompanying review. Numerical checks cover finitely many instances and do not establish the infinite theorem or historical priority.

## References
- J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. Freely accessible author PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (especially Section 5.3).
- S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819. DOI: 10.1137/070689413. Author PDF: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
- B. Gerencsér, J. Hendrickx, and P. Van Dooren, *Spectral Gap of Markov Chains on a Cycle*, European Control Conference (2015), 765–769. DOI: 10.1109/ECC.2015.7330635. Author manuscript: https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf.
