# Rational formality of the unordered two-point configuration space of CP^2

## Context
Let $F(CP^2,2)$ be the ordered configuration space of two distinct points in
the complex projective plane $CP^2$, and
$C_2(CP^2)=(F(CP^2,2))/S_2$ its unordered quotient by the free swap action.
Over $Q$, $CP^2$ is formal with $H^*(CP^2;Q)=Q[x]/(x^3)$, $|x|=2$.
Kriz, Totaro, Felix-Thomas, and Lambrechts-Stanley associate to such a
manifold an explicit commutative dg-algebra model built from
$H^*(M)^{\\otimes 2}$ plus an Arnold-type generator resolving the diagonal.
For general simply connected closed $M$ this model has nontrivial
differential and does not by itself decide formality.
The admitted target asks for a two-sided decision: either a nonzero triple
Massey product obstructing formality with a full ledger, or an explicit
formality zigzag to cohomology. The nearby prior formality corollary
(Lambrechts-Stanley AIF 2004, Cor. 6.1) requires $H^1(M)=H^2(M)=0$ and hence
does not apply to $CP^2$.

## Definitions
Let $R=Q[a,b]/(a^3,b^3)$ with $|a|=|b|=2$, modelling $H^*((CP^2)^2;Q)$.
Let $J=(R\\otimes \\Lambda(e),d)$ with $|e|=3$, relation $(a-b)e=0$,
$d(a)=d(b)=0$, $d(e)=\\Delta:=a^2+ab+b^2$.
$\\Delta$ is the diagonal class $x^2\\otimes 1+x\\otimes x+1\\otimes x^2$.
Swap $S_2: a\\leftrightarrow b$, $e\\mapsto e$ is a CDGA automorphism;
$J^s:=(J)^{S_2}$ over $Q$ models unordered $C_2(CP^2)$.
Write $s_1=a+b$, $p=a^2+b^2$, $q=ab$, $r=ab(a+b)=a^2b+ab^2$, $w=a^2b^2$.
Let $L=(\\Lambda(x,y),d_L)$ with $|x|=2$, $|y|=5$, $d_Lx=0$, $d_Ly=x^3$,
and $H=(Q[t]/(t^3),0)$ with $|t|=2$.

## Result
$C_2(CP^2)$ is formal over $Q$. Its rational cohomology is
$H^*(C_2(CP^2);Q)\\cong Q[t]/(t^3)$, $|t|=2$, concentrated in degrees
$0,2,4$. Its Sullivan minimal model is $(\\Lambda(x_2,y_5),dy=x^3)$.
There is an explicit quasi-isomorphism zigzag
$(H,0) \\xleftarrow{\\psi} L \\xrightarrow{\\phi} J^s$ with
$\\phi(x)=s_1$, $\\phi(y)=\\tfrac32 s_1e$ and $\\psi(x)=t$, $\\psi(y)=0$.
In particular every rational Massey product on $C_2(CP^2)$ vanishes
uniformly; branch (i) of the target (nonzero Massey ledger) is empty and
branch (ii) (formality zigzag) holds.

## Proof / evidence
Well-definedness: $(a-b)\\Delta=a^3-b^3=0$ in $R$, so $d((a-b)e)=0$ and $d$
descends; $d^2=0$ since $d(R)=0$ and $d^2(e)=d(\\Delta)=0$.
Symmetric bases of $J^s$ (monomials $a^ib^j$, $0\\le i,j\\le 2$, times $1$
or $e$, modulo $(a-b)e=0$): deg 0: $\\{1\\}$; deg 2: $\\{s_1\\}$;
deg 3: $\\{e\\}$; deg 4: $\\{p,q\\}$; deg 5: $\\{s_1e\\}$ (since $ae=be$);
deg 6: $\\{r\\}$; deg 7: $\\{qe\\}$ (since $a^2e=abe=b^2e$);
deg 8: $\\{w\\}$. Odd-quotient dimensions $\\dim R_d/(a-b)R_{d-2}=1$ in
degrees $3,5,7$ were recomputed independently by rank calculation.
Differentials (multiplication by $\\Delta$, using $a^3=b^3=0$):
$d(e)=p+q\\ne0$, $d(s_1e)=2r\\ne0$ (since $s_1\\Delta=2r$), $d(qe)=w\\ne0$
(since $q\\Delta=w$). Hence $H^3=H^5=H^7=0$, $H^6=\\mathrm{span}\\{r\\}/
\\mathrm{span}\\{2r\\}=0$, $H^8=\\mathrm{span}\\{w\\}/\\mathrm{span}\\{w\\}=0$,
$H^0=Q$, $H^2=\\mathrm{span}\\{s_1\\}$, $H^4=\\mathrm{span}\\{p,q\\}/
\\mathrm{span}\\{p+q\\}$, of dimension $1$ each; Euler number $3=6/2$.
Ring: $s_1^2=p+2q$ is linearly independent of $p+q$, so $[s_1]^2\\ne0$;
$s_1p=r$ and $s_1q=r$ give $s_1^3=3r=d(\\tfrac32 s_1e)$, so $[s_1]^3=0$.
Thus $H(J^s)=Q[t]/(t^3)$ with $t=[s_1]$.
$L$ is Sullivan minimal ($dy$ decomposable); $d(x^my)=x^{m+3}$ so
$H(L)=Q[x]/(x^3)$ in degrees $0,2,4$.
$\\phi$ is a CDGA map ($L$ free commutative) and chain map:
$\\phi(dy)=s_1^3=3r=d(\\tfrac32 s_1e)=d(\\phi(y))$; it sends $[x]\\mapsto[s_1]\\ne0$,
$[x]^2\\mapsto[s_1^2]\\ne0$, hence is a quasi-isomorphism between two
$Q[-]/(\\mathrm{cube})$ cohomologies in degrees $0,2,4$.
$\\psi$ is a chain map since $\\psi(dy)=t^3=0$, inducing the identity
$Q[x]/(x^3)\\to Q[t]/(t^3)$, a quasi-isomorphism.
Thus $J^s \\xleftarrow{\\phi} L \\xrightarrow{\\psi} (H,0)$ is a formality
zigzag. All identities were machine-checked over exact rationals.

## Limitations
Over rational coefficients $Q$ (hence real) only; no integral formality
claim. Covers unordered $n=2$ points in $CP^2$ specifically, not other
manifolds or $n\\ge 3$. Takes the published Kriz-Totaro/Lambrechts-Stanley
CDGA identification of $J$ and passage to $S_2$-invariants over $Q$ as the
input model.

## Reproducibility
Run `python3 output/artifacts/verify_formality.py`: checks nonvanishing of
the three differentials, $s_1^2=p+2q$ independence from $p+q$,
$s_1^3=3r=d((3/2)s_1e)$, the chain-map identity $\\phi(dy)=d(\\phi(y))$,
and cohomology-dimension counts on both sides. All checks use
`fractions.Fraction` exact arithmetic. An independent rank computation of
$R_d/(a-b)R_{d-2}$ confirms odd dimensions $1,1,1$ in degrees $3,5,7$.

## References
Lambrechts-Stanley, The rational homotopy type of configuration spaces of
two points, Ann. Inst. Fourier 54(4) 2004, 1029-1052.
Kriz, Rational homotopy type of configuration spaces, Invent. Math. 1994.
Totaro, Configuration spaces of algebraic varieties, Topology 1996.
Felix-Thomas; Cohen-Taylor; Idrissi, The Lambrechts-Stanley Model of
Configuration Spaces, arXiv:1608.08054; Deligne-Griffiths-Morgan-Sullivan
formality of compact Kahler manifolds.
