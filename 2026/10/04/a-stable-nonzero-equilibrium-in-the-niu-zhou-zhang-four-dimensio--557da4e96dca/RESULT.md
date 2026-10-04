# A stable nonzero equilibrium in the Niu–Zhou–Zhang four-dimensional flow
## Finding
For the four-dimensional autonomous flow
\[
\dot x=a(y-x)+z,\qquad
\dot y=bx-cy-xz,\qquad
\dot z=xy-dz+ew,\qquad
\dot w=fx+y,
\]
at the parameter vector used in Niu, Zhou and Zhang (2024),
\[
(a,b,c,d,e,f)=\left(34,28,\frac{13}{5},4,\frac{9}{5},\frac{12}{5}\right),
\]
the nonzero equilibrium is exactly
\[
E_*=\left(\frac{428}{1445},-\frac{5136}{7225},\frac{856}{25},\frac{1432077728}{18792225}\right).
\]
It is asymptotically stable. This reverses the source's local-stability classification of that equilibrium: the source reports a positive eigenvalue \(0.0501\) and concludes that both equilibria are unstable.

The corrected characteristic polynomial can be represented, up to a positive scalar factor, as
\[
P(\lambda)=10440125\lambda^4+423869075\lambda^3+4674655710\lambda^2+12506994792\lambda+643445784.
\]
Its quartic Routh–Hurwitz determinants satisfy
\[
\Delta_2=1850867402738339250>0,
\]
and
\[
\Delta_3=23033184284619159659128251000>0.
\]
Together with positivity of all five coefficients, these inequalities place every root strictly in the open left half-plane. Numerically,
\[
\operatorname{spec}J(E_*)\approx\{-24.0472952875,-12.6341098144,-3.8661238653,-0.0524710329\}.
\]
Thus \(E_*\) has an open attracting basin. If the chaotic or hyperchaotic invariant set displayed by the source exists at the same parameters, it necessarily coexists with this stable steady-state basin.

## Assumptions and scope
The claim concerns the smooth ordinary differential equation printed by Niu, Zhou and Zhang and the single parameter vector above. It is a local statement at the nonzero equilibrium. The conclusion uses standard linearization theory for a hyperbolic equilibrium: a Jacobian whose spectrum lies strictly in the left half-plane yields local asymptotic stability.

No claim is made that the source's displayed chaotic trajectory is nonexistent. The result instead shows that the published parameter choice is locally multistable whenever that chaotic invariant set is present, because an open neighborhood of \(E_*\) converges to \(E_*\).

## Proof
At an equilibrium, the fourth equation gives \(y=-fx\). Substituting into the first equation gives \(z=a(f+1)x\). For a nonzero equilibrium, the second equation becomes
\[
b+cf-z=0,
\]
so \(z=b+cf=856/25\) and
\[
x=\frac{b+cf}{a(f+1)}=\frac{428}{1445},\qquad y=-fx=-\frac{5136}{7225}.
\]
The third equation then yields
\[
w=\frac{fx^2+dz}{e}=\frac{1432077728}{18792225}.
\]
Direct substitution makes all four components of the vector field vanish exactly.

The Jacobian is
\[
J(x,y,z,w)=
\begin{pmatrix}
-a&a&1&0\\
b-z&-c&-x&0\\
y&x&-d&e\\
f&1&0&0
\end{pmatrix}.
\]
Evaluating at \(E_*\) and expanding \(\det(\lambda I-J(E_*))\) gives the positive multiple \(P(\lambda)\) displayed above. For a quartic \(A_4\lambda^4+A_3\lambda^3+A_2\lambda^2+A_1\lambda+A_0\) with positive leading coefficient, the Routh–Hurwitz test requires positivity of the coefficients together with
\[
A_3A_2-A_4A_1>0
\]
and
\[
A_3A_2A_1-A_4A_1^2-A_3^2A_0>0.
\]
The exact integer evaluations are precisely \(\Delta_2\) and \(\Delta_3\) above, both strictly positive. Hence every eigenvalue has negative real part, proving asymptotic stability.

## Verification
The bundled `verify.py` uses only the Python standard library. It reconstructs \(E_*\) as exact rational numbers, verifies the four equilibrium equations, expands \(\det(\lambda I-J(E_*))\) from the matrix entries, checks the primitive integer polynomial, and evaluates both quartic Hurwitz determinants exactly. It also computes approximate roots only as a readability check; the stability proof is the exact Hurwitz certificate. Running

`python3 verify.py`

returns `VERIFY_OK`.

## Relationship to prior work
Niu, Zhou and Zhang introduce the exact four-dimensional vector field, give the same numerical equilibrium coordinates, print the same Jacobian formula, and report the nonzero-equilibrium eigenvalues as approximately \(-24.1106,-12.4377,-4.1019,0.0501\), concluding that both equilibria are unstable. The exact calculation above changes the sign of the small eigenvalue and therefore changes the qualitative local dynamics.

Searches of the published-finding corpus corpus by the source DOI, exact equilibrium coordinates, vector-field form, and stability language did not return a source-specific result implying this correction. Exact web searches for the DOI together with “equilibrium stability”, for the distinctive coordinates, and for the printed vector-field form likewise located the source and downstream reuse of the same chaotic generator but no prior correction of the nonzero equilibrium's stability.

The result is not a generic restatement of the Routh–Hurwitz criterion: its content is the exact application to this published generator, where the sign error changes the existence of a stable steady-state basin at the very parameter set used for the claimed hyperchaotic pseudorandom source.

## Limitations
This is a local equilibrium result. It does not determine the size or geometry of the basin of \(E_*\), does not establish or refute a separate chaotic invariant set, and does not reassess the encryption algorithm as a whole. The literature search cannot logically prove absence of every unpublished or unindexed prior correction; it supports the originality assessment only to the extent of the inspected sources and databases.

## References
1. Y. Niu, H. Zhou, X. Zhang, “Image encryption scheme based on improved four-dimensional chaotic system and evolutionary operators,” *Scientific Reports* 14, 7033 (2024), DOI: 10.1038/s41598-024-57756-x. Published 25 March 2024.
2. MSC2020, 37C10, “Dynamics induced by flows and semiflows,” Mathematical Reviews/zbMATH classification database.
