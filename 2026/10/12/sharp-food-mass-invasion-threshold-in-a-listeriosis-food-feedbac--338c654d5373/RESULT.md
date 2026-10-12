# Sharp food-mass invasion threshold in a listeriosis–food feedback model

## Finding

Consider the listeriosis-only five-compartment equations (4.1) of Koutou, Kouanda and Ouédraogo (2026), exactly as printed, on a conserved positive-food-mass leaf \(U+C=F>0\). For every choice of strictly positive rate parameters, the number of equilibria with **all five components strictly positive** is either zero or one, determined by a sharp threshold that incorporates contaminated-food feedback absent from the source's reported threshold.

Set \(h=\mu+\delta+\gamma\), \(k=\xi/d\), \(\Delta=p-a_4F\), and \(\widehat{\mathcal R}=\beta k\Lambda/(\mu h)\). If \(\Delta>0\), define
\[
\mathcal T_F=\widehat{\mathcal R}\left(1+\frac{a_3F}{\Delta}\right).
\]
There is exactly one strictly positive equilibrium **if and only if** \(\mathcal T_F>1\); none exists when \(\mathcal T_F\leq1\). The unique disease-free equilibrium on this food-mass leaf is locally asymptotically stable if \(\mathcal T_F<1\), linearly unstable if \(\mathcal T_F>1\), and nonhyperbolic at equality.

If \(\Delta\leq0\), a strictly positive equilibrium exists uniquely for **every positive transmission coefficient** \(\beta\), and the disease-free equilibrium is linearly unstable. No global stability or endemic-orbit stability assertion is made.

In particular, \(\Lambda=\mu=\delta=\gamma=\xi=d=p=a_3=a_4=1\), \(\beta=2\), and \(F=9/10\) give the source's \(\widehat{\mathcal R}=2/3<1\), yet \(\mathcal T_F=20/3>1\) and the exact positive equilibrium
\[
(S,I,B,U,C)=\left(\frac35,\frac15,\frac15,\frac35,\frac3{10}\right).
\]
Thus Proposition 4.2 of the motivating publication does not hold as an if-and-only-if criterion on every physically positive fixed-food-mass leaf.

## Assumptions and scope

The state \((S,I,B,U,C)\) consists of susceptible humans, infected humans, environmental bacteria, uncontaminated food and contaminated food. All nine rates and the recruitment \(\Lambda\) listed here are strictly positive; \(F>0\) is a fixed mass, not a rate parameter. The exact autonomous differential equations, with dots indicating time derivatives, are
\[
\begin{aligned}
\dot S&=\Lambda+\gamma I-(\mu+\lambda)S,\\
\dot I&=\lambda S-hI,\\
\dot B&=\xi I-dB,\\
\dot U&=p(U+C)-(B+a_4C+p)U,\\
\dot C&=(B+a_4C)U-pC,\\
\lambda&=\beta(B+a_3C),\qquad h=\mu+\delta+\gamma.
\end{aligned}
\]
Here \(\Lambda,\mu,\delta,\gamma,\beta,\xi,d,p,a_3,a_4>0\). These equations form the **standalone listeriosis-only model (4.1)**; they are not asserted to form an invariant positive-parameter subsystem of the larger eight-compartment co-infection model. The sum \(U+C=F\) is constant because \(\dot U+\dot C=0\). All stability statements are restricted to the four-dimensional invariant leaf \(U+C=F\): in the unrestricted five-dimensional system the conservation law supplies a neutral direction.

The disease-free equilibrium on this leaf is \(E_0=(\Lambda/\mu,0,0,F,0)\). The source's formula (4.2) is \(\widehat{\mathcal R}\), which does not include the food-feedback parameters \(a_3,a_4,p,F\). The new threshold \(\mathcal T_F\) is referred to as a **linear invasion index**; we do not assert it is a uniquely normalized next-generation reproduction number.

## Proof

**1. Reduction to one scalar equation.** At equilibrium, adding the human equations and using \(\dot B=0\) yields
\[
S=\frac{\Lambda-(\mu+\delta)I}{\mu},\qquad B=kI,\qquad
0<I<I_{\max}:=\frac{\Lambda}{\mu+\delta},\quad k=\frac\xi d.
\]
The food equations reduce to the single equation \(\dot C=(B+a_4C)(F-C)-pC=0\), equivalently
\[
q(C;B):=a_4C^2+(B+\Delta)C-BF=0,\qquad \Delta=p-a_4F.
\]
For every \(B>0\), \(q(0;B)=-BF<0\), \(q(F;B)=pF>0\), and the quadratic has one positive and one negative root. Hence there is exactly one root \(C(B)\in(0,F)\). Put \(U(B)=F-C(B)>0\). At that root,
\[
D(B):=\frac{\partial q}{\partial C}=B+\Delta+2a_4C(B)
=\frac{BF+a_4C(B)^2}{C(B)}>0.
\]
Implicit differentiation therefore gives
\[
C'(B)=\frac{F-C(B)}{D(B)}>0,\qquad
C''(B)=-\frac{2C'(B)\bigl(1+a_4C'(B)\bigr)}{D(B)}<0.
\]
In particular, \(C(B)\) is strictly increasing and strictly concave on \((0,\infty)\). Its nonnegative limit at zero, together with strict concavity, implies \(BC'(B)<C(B)\) for \(B>0\), so \(C(B)/B\) is strictly decreasing.

For \(I>0\) the infected-human equilibrium equation, after inserting the preceding expressions and dividing by \(I\), is
\[
\underbrace{\beta\left(k+a_3\frac{C(kI)}I\right)}_{\text{strictly decreasing in }I}
=\underbrace{\frac{h\mu}{\Lambda-(\mu+\delta)I}}_{\text{strictly increasing in }I},\qquad 0<I<I_{\max}.
\]
The left side is finite at each positive \(I\), whereas the right side tends to \(+\infty\) as \(I\uparrow I_{\max}\). Thus there can be **at most one** positive solution. Any such solution reconstructs all five strictly positive equilibrium components using the explicit identities above, and every positive equilibrium must arise in this way.

**2. Sharp existence boundary.** The food balance can also be written
\[
B\bigl(F-C(B)\bigr)=C(B)\bigl(\Delta+a_4C(B)\bigr).
\]
If \(\Delta>0\), then \(C(B)\downarrow0\) as \(B\downarrow0\), and \(C(B)/B\to F/\Delta\). Therefore the decreasing side of the scalar equilibrium equation tends to \(\beta k(1+a_3F/\Delta)\) at \(I=0+\). The increasing side tends to \(h\mu/\Lambda\). Strict monotonicity and continuity show that the sides cross at exactly one positive \(I\) if and only if \(\mathcal T_F>1\). Equality gives no positive crossing because the first side strictly decreases and the second increases on the open interval.

If \(\Delta=0\), the food equation forces \(C(B)\to0\) and \(C(B)^2/B\to F/a_4\), hence \(C(B)/B\to\infty\). If \(\Delta<0\), the unique positive food branch tends to \(-\Delta/a_4=F-p/a_4>0\), and again \(C(B)/B\to\infty\). In both cases the left side of the equilibrium equation diverges at \(I=0+\), so a unique crossing exists for every \(\beta>0\).

**3. Disease-free linear threshold on the correct leaf.** In coordinates \((S,I,B,C)\) with \(U=F-C\), linearization at \(E_0\) has a scalar susceptible eigenvalue \(-\mu\) and the infected/environmental Metzler block
\[
M_F=\begin{pmatrix}
-h&\beta\Lambda/\mu&\beta a_3\Lambda/\mu\\
\xi&-d&0\\
0&F&-\Delta
\end{pmatrix}.
\]
For \(\Delta>0\), the strictly positive vector \(w=(1,k,kF/\Delta)^{\mathsf T}\) satisfies
\[
M_Fw=\bigl(h(\mathcal T_F-1),0,0\bigr)^{\mathsf T}.
\]
When \(\mathcal T_F<1\), choose a sufficiently small positive perturbation of the second and third entries of \(w\) so that all three entries of \(M_Fw\) become strictly negative. This is possible explicitly by first increasing the second coordinate slightly, then increasing the third coordinate slightly more than \(F/\Delta\) times that increase, with the original strict first-row negative margin retained. A Metzler matrix with \(M_Fv<0\) for a strictly positive vector \(v\) is Hurwitz (diagonal similarity and the maximum-component norm give exponential decay). When \(\mathcal T_F>1\), instead decrease the second coordinate slightly and decrease the third coordinate slightly further so that \(M_Fv>0\); comparison with an exponentially growing positive vector then shows a positive spectral bound. At equality, \(M_Fw=0\), so the equilibrium is nonhyperbolic.

For \(\Delta\leq0\), take \(v=(1,k/2,c)^{\mathsf T}\) with \(c>0\) sufficiently large. Then every component of \(M_Fv\) is strictly positive: the second equals \(\xi/2\), the third is \(Fk/2-\Delta c>0\), and the first is positive for large \(c\). Thus the Metzler comparison argument again gives a positive growth rate and linear instability. This completes the threshold and uniqueness proof.

**4. Exact counterexample to the printed criterion.** With the positive parameters displayed in the Finding, \(\Delta=1/10\), \(k=1\), \(h=3\), \(\widehat{\mathcal R}=2/3\), and \(\mathcal T_F=20/3\). At the claimed equilibrium, \(\lambda=2(1/5+3/10)=1\). The five right-hand sides, in their displayed order, are
\[
1+\frac15-2\frac35=0,\quad \frac35-3\frac15=0,\quad \frac15-\frac15=0,\quad
\frac9{10}-\frac32\frac35=0,\quad \frac12\frac35-\frac3{10}=0.
\]
All five state components are positive and \(U+C=9/10\). The old inequality \(\widehat{\mathcal R}<1\) does not exclude this endemic equilibrium; the new criterion correctly predicts it.

## Verification

Run `python verify.py` after installing the explicitly listed package in `requirements.txt`. The checker evaluates the exact rational witness, its five differential right-hand sides, the conserved food and human balance identities, the symbolic food quadratic, the disease-free Jacobian, and the positive-vector threshold identity. The verified output is `VERIFY_OK`. These computational identities supplement, but do not replace, the analytic proof of existence and uniqueness for **all** positive parameters. No numerical integration, finite-state census, or outsourced mathematical certification is used.

## Relationship to prior work

Koutou–Kouanda–Ouédraogo (2026), equations (4.1)–(4.6), proves results for the same printed listeriosis-only system but states in Proposition 4.2 that a unique endemic equilibrium exists iff their \(\widehat{\mathcal R}>1\). Their formula omits feedback through contaminated food on the conserved positive-food leaf. The theorem above supplies the corrected all-parameter criterion and a rational counterexample, rather than claiming to discover foodborne transmission or general epidemic thresholds.

Chukwu–Nyabadza (2020) and Chukwu–Nyabadza–Fatmawati (2021) already model food cross-contamination and identify distinct food-contamination thresholds. The 2020 model includes workers and autonomous environmental Listeria growth; the 2021 media-campaign model also uses autonomous bacterial growth and open food replenishment. Neither establishes the conserved-food closed human–bacteria–food loop criterion of equations (4.1). Omar and colleagues (2026) consider a different eight-state risk-stratified model with externally recruited food and logistic bacterial dynamics, not the conserved-food setting. Chukwu–Mushanyu–Juga–Fatmawati (2020) model listeriosis/meningitis co-dynamics without this pair of explicit food compartments. Van den Driessche–Watmough (2002) give the foundational general next-generation threshold theory; the local Metzler criterion here is an application of standard ideas, while the complete nonlinear positive-equilibrium count and the precise omitted feedback are the specific contribution. A source search cannot exclude every unindexed result.

## Limitations

The proof addresses only the printed **standalone** system (4.1), positive initial food mass, strictly positive rates, equilibrium counting and local disease-free stability. It does not prove global convergence, the positive equilibrium's stability, any claim about a full eight-state co-infection system with nonzero meningitis transmission, or empirical epidemiological conclusions. The linear threshold is a mathematical parameter criterion, not a newly calibrated biological reproduction number. The conservation law means any use of local asymptotic stability must be restricted to a fixed-\(F\) leaf. No independent audit has been performed.

## References

1. O. Koutou, C. A. K. Kouanda and A. Ouédraogo, “Mathematical Analysis of a Co-Dynamics Model of Listeriosis and Bacterial Meningitis Starting From Ready-to-Eat Foods,” *International Journal of Analysis and Applications* **24** (2026), article 160, DOI: 10.28924/2291-8639-24-2026-160. Published 2026-05-20. Full text: https://www.etamaths.com/index.php/ijaa/article/download/4183/1735.
2. C. W. Chukwu and F. Nyabadza, “A Theoretical Model of Listeriosis Driven by Cross Contamination of Ready-to-Eat Food Products,” *International Journal of Mathematics and Mathematical Sciences* **2020**, article 9207403, DOI: 10.1155/2020/9207403.
3. C. W. Chukwu, F. Nyabadza and Fatmawati, “Modelling the Potential Role of Media Campaigns on the Control of Listeriosis,” *Mathematical Biosciences and Engineering* **18** (2021), 7580–7601, DOI: 10.3934/mbe.2021375. Full text: https://www.aimspress.com/aimspress-data/mbe/2021/6/PDF/mbe-18-06-375.pdf.
4. H. A. Omar, M. Abdullahi, A. Abdullahi and U. Gidado, “Mathematical Analysis and Optimal Control of Listeriosis Transmission in a Coupled Human-Food-Bacteria System,” *International Journal of Development Mathematics* **3** (2026), 107–131, DOI: 10.62054/ijdm/0303.06. Full text: https://ijdm.org.ng/index.php/Journals/article/download/378/351/4092.
5. C. W. Chukwu, J. Mushanyu, M. L. Juga and Fatmawati, “A Mathematical Model for Co-Dynamics of Listeriosis and Bacterial Meningitis Diseases,” *Communications in Mathematical Biology and Neuroscience* **2020**, article 83, DOI: 10.28919/cmbn/5060.
6. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* **180** (2002), 29–48, DOI: 10.1016/S0025-5564(02)00108-6. Author-hosted full text: https://watmough.ext.unb.ca/papers/mgroup.pdf.
