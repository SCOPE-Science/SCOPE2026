# Disproof of coprime ray ring class generation by Hayes A-torsion

## Context

Let $A=\mathbf{F}_q[T]$, $F=\mathbf{F}_q(T)$, and $K/F$ an imaginary quadratic
function field. Write $\mathcal{O}_f$ for the $A$-order of conductor $f$ and
$j_{\mathrm{CM}}$ for the $j$-invariant of a rank-2 Drinfeld $A$-module with
CM by $\mathcal{O}_f$. Let $\psi$ be a sign-normalized rank-1 Hayes
$A$-module. A natural guess is that, for $m \triangleleft A$ coprime to $f$,
adjoining the $A$-module $m$-torsion $\psi[m]$ to $K(j_{\mathrm{CM}})$ yields
the ray ring class field of $\mathcal{O}_f$ modulo $m\mathcal{O}_f$, with
relative degree $|(\mathcal{O}_f/m\mathcal{O}_f)^*|/|\mathbf{F}_q^*|$ up to the
unit index. The result below refutes this law as stated with one explicit
tuple, and diagnoses the defect as a rank mismatch.

## Definitions

- $q=3$, $A=\mathbf{F}_3[T]$, $F=\mathbf{F}_3(T)$,
  $K=F(U)$ with $U^2+T=0$, i.e. $K=\mathbf{F}_3(U)$.
- $\mathcal{O}_f=\mathcal{O}_K=\mathbf{F}_3[U]$ (conductor $f=1$), $m=(T)$.
- Carlitz module $\rho_T(x)=Tx+x^3$ (the sign-normalized rank-1 Hayes module).
- CM module $\phi_T=T-(U+U^3)\tau-\tau^2$ with $\psi_U=U+\tau$,
  $\tau$ Frobenius at $q=3$.
- $j_{\mathrm{CM}}=-(U+U^3)^4$.

## Result

The coprime ray ring class generation law is FALSE as stated.
For the tuple above: $K(j_{\mathrm{CM}})=K$ and
$K(j_{\mathrm{CM}})(\psi[(T)])=K$, so the actual relative degree is $1$,
whereas the law predicts $|(\mathcal{O}_K/(T))^*|/|\mathbf{F}_3^*|=6/2=3$.
Moreover the left-hand side is unramified at $(U)\mid(T)$ while the genuine
conductor-$(T)$ ray field is ramified there, so the field identity fails too.

## Proof / evidence

Coprimality holds since $f=1$. The prime $(T)$ ramifies in $K$ as
$(T)=(U)^2$. Since $\tau U=U^3\tau$,
$\psi_U^2=U^2+(U+U^3)\tau+\tau^2=-\phi_T$ using $T=-U^2$; hence $U$
satisfies $X^2+T=0$ in $\mathrm{End}(\phi)$, so $\phi$ is a rank-2 Drinfeld
module with CM by $\mathcal{O}_K=\mathbf{F}_3[U]$, which is integrally closed
because $K$ is rational. Its $j$-invariant $j_{\mathrm{CM}}=-(U+U^3)^4$ lies
in $K^\times$ and is nonzero, so $K(j_{\mathrm{CM}})=K$; also
$h(\mathcal{O}_K)=1$, so the unramified ring class field is $K$ itself.

The Carlitz $(T)$-torsion equation $\rho_T(x)=x(x^2+T)=0$ has roots
$0,U,-U$ in $K$ since $U^2=-T=(-U)^2$. Hence all $(T)$-torsion already lies
in $K$ and $[K(j_{\mathrm{CM}})(\psi[(T)]):K(j_{\mathrm{CM}})]=1$.

Meanwhile $\mathcal{O}_K/(T)=\mathbf{F}_3[U]/(U^2)$ has $9$ elements $a+bU$
with units those with $a\ne 0$, so
$|(\mathcal{O}_K/(T))^*|=2\cdot 3=6$. Since
$\mathcal{O}_K^*=\mathbf{F}_3^*$, the unit index is $1$ and the law predicts
degree $6/2=3$, contradicting the actual degree $1$.

For ramification, $C_U(x)=Ux+x^3$ and
$C_{U^2}(x)=x^9+(U+U^3)x^3+U^2x$ satisfy
$C_{U^2}(x)/C_U(x)=x^6-Ux^4+U^2x^2+U$, verified by expansion. As a cubic in
$y=x^2$, $y^3-Uy^2+U^2y+U$ is Eisenstein at $(U)$, hence irreducible and
totally ramified of degree $3$ at $(U)$. The true ray ring class field has
degree $3$ (ray class group $(\mathcal{O}_K/(T))^*/\mathbf{F}_3^*$ of order
$3$ with $h=1$) and is ramified at $(U)$; the left-hand side $K/K$ is
trivial, hence unramified. Both the degree law and the field identity fail.

The defect is the rank: $\psi[m]$ is $A$-torsion, seeing only
$|(A/m)^*|$ (here $|(A/(T))^*|/|\mathbf{F}_3^*|=1$), while the modulus
$m\mathcal{O}_f$ side sees $|(\mathcal{O}_f/m\mathcal{O}_f)^*|$. The
$\mathcal{O}_f$-torsion (CM division field) does produce the ramified
degree-3 extension.

## Limitations

This is a disproof of the stated $A$-torsion law only. It does not prove a
corrected law; the remark that $\mathcal{O}_f$-torsion plausibly generates
the ray field is a conjecture supported by the Eisenstein certificate but
not proved here. Computations are exact finite-field polynomial identities.

## Reproducibility

The stdlib-only script `artifacts/verify_counterexample.py` checks the unit
count $6$, the Ore relation $\phi_T+\psi_U^2=0$, the splitting of $\rho_T$
over $K$, the quotient identity, and the Newton/Eisenstein ramification
certificate. All assertions pass.

## References

- D. Hayes, Explicit class field theory for rational function fields (1974).
- D. Goss, Basic Structures of Function Field Arithmetic.
- D. Zywina, Explicit class field theory for global function fields.
- L. Demangos, T. M. Gendron, Explicit class field theory for orders in
  global function fields, arXiv:2407.09319 (Hayes theory for orders; ray
  generation uses R-torsion).
