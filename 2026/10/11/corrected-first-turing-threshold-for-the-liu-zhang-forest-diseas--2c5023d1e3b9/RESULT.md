# Corrected first Turing threshold for the Liu–Zhang forest-disease-fire model
## Finding
For the reaction–diffusion system printed in Liu and Zhang (2024), use the numerical parameters
\[
r=0.721,\quad K=90,\quad \sigma=0.601,\quad \alpha=37.8537234,\quad \beta=0.318,\quad \omega=0.055,\quad \mu=0.02.
\]
At the value \(d=0.12\) explicitly analyzed in Section 4.3, the first Turing crossing of the printed modal characteristic matrix is
\[
\varepsilon_c=0.00852879885272517\ldots,
\]
in spatial mode \(k=1\). The paper instead reports \(\varepsilon=0.0011360854\).

The same reconstruction also changes the underlying positive equilibrium. The printed reaction equations have the unique positive equilibrium
\[
E_*=(S_*,I_*)=(17.4074329451502\ldots,\;238.924460427888\ldots),
\]
not the point \((17.252,236.374)\) stated in Section 4.3. At the paper's quoted threshold, the corrected mode-1 linearization already has a positive eigenvalue
\[
\lambda_+=0.008760101432709\ldots.
\]
Thus the reported number is not a bifurcation point of the printed model.

There is also a model-independent internal check on the arithmetic: if one accepts the paper's own rounded coefficients \(p_1=0.0120\), \(q_1=-0.0028\), \(p_2=0.2740\), \(q_2=-0.0172\), its displayed formula for \(\varepsilon_*(k,d)\) gives
\[
\varepsilon_*(1,0.12)=0.00959299911177703\ldots,
\]
not \(0.0011360854\).

## Assumptions and scope
The claim concerns the equations and modal matrix printed in Sections 4.1–4.3 and the explicit choice \(d=0.12\). The source uses modal Laplacian eigenvalues \(k^2\pi^2\), and this calculation follows that convention exactly. It is a linear stability statement about the homogeneous positive equilibrium.

The claim does not infer which diffusion coefficients were actually used to generate Figures 5–6. Section 4.3 first lists \(D_S=0.03\) and \(D_I=0.41\), then separately chooses \(d=0.12\); that implementation ambiguity is left unresolved. No nonlinear existence, amplitude, or stability theorem for a patterned branch is claimed.

## Proof
For a positive equilibrium, the second printed reaction equation gives
\[
I=\frac{\beta}{\mu}S-\alpha.
\]
Substitution into the first equilibrium equation and multiplication by the positive denominator \(S(1+\omega S)\) gives the cubic
\[
-\frac{7931}{18000000}S^3+\frac{25477}{1800000}S^2-\frac{7818045213}{50000000000}S+\frac{189268617}{250000000}=0.
\]
Its discriminant is
\[
-\frac{2162092641975697274040368003450789}{15187500000000000000000000000000000000000}<0,
\]
so it has exactly one real root. Since the polynomial changes sign between \(17\) and \(18\), that root is positive. Solving it and using the relation for \(I\) gives the stated \(E_*\).

At this equilibrium, the derivatives appearing in the source's modal matrix are
\[
\begin{aligned}
p_1&=0.01072598427642497\ldots, & q_1&=-0.002735311206719895\ldots,\\
p_2&=0.2745085518131537\ldots, & q_2&=-0.01726468879328010\ldots.
\end{aligned}
\]
Let \(\Delta_0=p_1q_2-p_2q_1=0.0005656855375808754\ldots>0\) and \(x_k=d k^2\pi^2\). The printed determinant reduces exactly to
\[
\operatorname{DET}_k(\varepsilon)=\varepsilon x_k(x_k-q_2)-p_1x_k+\Delta_0.
\]
Because the trace is
\[
\operatorname{TR}_k=-(1+\varepsilon)x_k+p_1+q_2<0,
\]
a modal stability loss occurs precisely when \(\operatorname{DET}_k\) crosses zero. The positive root is
\[
\varepsilon_k=\frac{p_1x_k-\Delta_0}{x_k(x_k-q_2)}.
\]
Writing the right-hand side as \(\phi(x)\), its derivative has numerator
\[
-p_1x^2+2\Delta_0x-\Delta_0q_2.
\]
The positive zero of this quadratic is \(0.113501680812333\ldots\), whereas \(x_1=0.12\pi^2=1.18435252813072\ldots\). Hence \(\phi\) is strictly decreasing for every \(x\ge x_1\), so \(\varepsilon_1\) is the largest modal crossing and therefore the first loss of stability as \(\varepsilon\) decreases. Direct substitution gives the stated \(\varepsilon_c\).

At \(\varepsilon_c\), \(\operatorname{DET}_1=0\) and the companion eigenvalue is \(\operatorname{TR}_1=-1.20099233713072\ldots<0\). At the paper's quoted \(\varepsilon=0.0011360854\), instead \(\operatorname{DET}_1=-0.0105208543113012\ldots<0\), yielding one positive eigenvalue \(0.008760101432709\ldots\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It checks the exact cubic discriminant, brackets and solves the unique real equilibrium, recomputes the four Jacobian entries, checks that the derivative turnover lies below the first spatial mode, evaluates the corrected threshold, and separately evaluates the source's rounded-coefficient formula. Successful replay prints `VERIFY_OK`.

As an independent arithmetic cross-check, the paper's own displayed rounded formula
\[
\varepsilon_*(k,d)=\frac{0.012\,d k^2\pi^2-0.0005608}{d k^2\pi^2(d k^2\pi^2+0.0172)}
\]
gives \(0.00959299911177703\ldots\) at \((k,d)=(1,0.12)\).

## Relationship to prior work
Liu and Zhang derive the modal trace and determinant and explicitly state that, at \(d=0.12\), the system undergoes a Turing bifurcation at \(\varepsilon=0.0011360854\). The present calculation does not replace their general determinant formula; it corrects the Section 4.3 numerical specialization by enforcing the printed equilibrium equations and then evaluating that same modal determinant.

A closely related paper by Chen and Zhang (2022), cited by Liu and Zhang for reaction–diffusion bifurcation analysis, develops Turing and Turing–Hopf thresholds for a different Leslie–Gower predator–prey system. Full-text comparison shows a different state system, equilibrium, diffusion parameters, and critical curves; it does not state or imply the corrected forest-model numbers above. Exact searches for the DOI, the reported numerical threshold, the reported equilibrium pair, and correction/erratum terminology did not locate a published correction of this Section 4.3 calculation.

## Limitations
This is a correction of a source-specific linear calculation, not a new general Turing theorem. It does not validate the spatial domain or boundary conditions omitted from the displayed forest model, does not identify the diffusion coefficients actually used in the figures, and does not establish a nonlinear branch of patterned steady states. The source's Figure 6 value \(\varepsilon=0.00111725\) remains on the unstable side of the corrected threshold, so the qualitative observation of instability at that smaller value is not contradicted by this result.

## References
1. X. Liu and C. Zhang, “Forest model dynamics analysis and optimal control based on disease and fire interactions,” *AIMS Mathematics* 9(2) (2024), 3174–3194. DOI: 10.3934/math.2024154. See Sections 4.1–4.3, especially pp. 3182–3186.
2. H. Chen and C. Zhang, “Dynamic analysis of a Leslie–Gower-type predator–prey system with the fear effect and ratio-dependent Holling III functional response,” *Nonlinear Analysis: Modelling and Control* 27(5) (2022), 904–926. DOI: 10.15388/namc.2022.27.27932.
