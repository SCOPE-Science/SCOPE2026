# Frobenius collapse of two-call passive register programs in positive characteristic

## Result

Let \(K\) be a field, and consider a univariate passive-output register program with exactly two registers: one work register \(U\) and one output register \(O\). Basic instructions have the form permitted in the register-program model,
\[
R_i\leftarrow R_i+p(\text{other registers}),
\]
and an input access adds \(\lambda x\) to a register. The output register is passive, so it never appears on the right-hand side of an instruction. A clean program must restore \(U\) to its arbitrary initial value and add the computed polynomial to \(O\).

Call \(A\in K[X]\) additive when the polynomial identity
\[
A(X+Y)=A(X)+A(Y)
\]
holds in \(K[X,Y]\).

**Theorem.** A polynomial \(f\in K[X]\) is cleanly computable by a passive-output program with two registers and at most two input accesses if and only if
\[
f(X)=c+A(X)
\]
for some \(c\in K\) and some additive polynomial \(A\in K[X]\).

Consequently:

1. If \(\operatorname{char} K=0\), the only additive polynomials are \(A(X)=aX\), recovering the two-access degree-one frontier.
2. If \(\operatorname{char} K=p>0\), the additive polynomials are exactly
   \[
   A(X)=\sum_{j=0}^s a_j X^{p^j}.
   \]
   Hence, for every \(e\ge 1\), the monomial \(X^{p^e}\) has a clean passive program using two registers and exactly two nonzero input accesses.
3. In particular, over every infinite field of characteristic \(p>0\),
   \[
   D^{\mathrm{pass}}_{2,K}(2)=\infty,
   \]
   and therefore \(D^{\mathrm{pass}}_{r,K}(t)=\infty\) for every \(r\ge2\) and \(t\ge2\), if \(D^{\mathrm{pass}}\) is interpreted as in the motivating work. Over finite fields, polynomial functions have non-unique representatives, so degree itself is representation-dependent; nevertheless the construction below is a formal polynomial identity and gives arbitrarily large formal degree without relying on that ambiguity.

Thus the characteristic-zero lower bounds of Vinciguerra do not merely lose a constant factor in positive characteristic: the degree-versus-access frontier collapses completely once two input accesses are available.

## Proof

### Sufficiency

Let
\[
f(X)=c+A(X)
\]
with \(A\) additive. Start from arbitrary register contents
\[
U=\tau,\qquad O=\omega.
\]
Execute
\[
\begin{array}{rcl}
O&\leftarrow&O+c,\\
U&\leftarrow&U+x,\\
O&\leftarrow&O+A(U),\\
U&\leftarrow&U-x,\\
O&\leftarrow&O-A(U).
\end{array}
\]
The two updates of \(U\) are the only input accesses. At termination \(U=\tau\), while
\[
O=\omega+c+A(\tau+x)-A(\tau)
 =\omega+c+A(x)
 =\omega+f(x).
\]
The output is passive throughout, because it is never read. Hence the program is clean.

In characteristic \(p>0\), taking \(A(X)=X^{p^e}\) gives the particularly short identity
\[
(\tau+x)^{p^e}-\tau^{p^e}=x^{p^e}.
\]

### Necessity

Suppose a clean passive program with registers \(U,O\) uses at most two input accesses and computes \(f\).

Because \(O\) is passive, any basic instruction targeting \(U\) cannot read \(O\). With only two registers, such an instruction can therefore add only a constant to \(U\). It follows that the coefficient of \(x\) in \(U\) changes only at input accesses directed to \(U\).

If fewer than two nonzero accesses are directed to \(U\), cleanliness forces the \(x\)-coefficient of \(U\) to be zero throughout. Every basic update of \(O\) is then independent of \(x\), while direct input accesses to \(O\) contribute only a linear term. Thus \(f\) is affine linear, and the conclusion holds.

The only remaining case has two nonzero accesses to \(U\). Their coefficients must be \(a\) and \(-a\) with \(a\ne0\), since \(U\) must be restored. There are then no remaining input accesses to \(O\). Before the first access and after the second, \(U\) is of the form \(\tau+c\); between the two accesses it is of the form
\[
\tau+c+ax.
\]
All basic updates of \(O\) before and after the active interval can be collected into one polynomial \(B(\tau)\). All updates during the active interval can, after absorbing their constant shifts into their polynomial arguments, be collected into one polynomial \(H(\tau+ax)\). Hence cleanliness gives a polynomial identity
\[
B(\tau)+H(\tau+ax)=f(x).
\]
Setting \(x=0\) and subtracting yields
\[
H(\tau+ax)-H(\tau)=f(x)-f(0).
\]
Since \(a\ne0\), write \(y=ax\). The left-hand side depends only on \(y\), so setting \(\tau=0\) gives
\[
H(\tau+y)-H(\tau)=H(y)-H(0).
\]
Therefore
\[
A(Z):=H(Z)-H(0)
\]
satisfies
\[
A(\tau+y)=A(\tau)+A(y),
\]
so \(A\) is additive. Finally,
\[
f(x)-f(0)=A(ax),
\]
which is again additive. Thus \(f\) is a constant plus an additive polynomial.

The classical classification of additive polynomials now gives the characteristic dichotomy: they are linear in characteristic zero, while in characteristic \(p>0\) they are precisely the linearized polynomials \(\sum_j a_jX^{p^j}\).

## Relation to recent work

Vinciguerra's 2026 paper *An Operator Approach to Register Programs for Catalytic Computing* studies the same register-program model. Section 3 is explicitly restricted to characteristic zero. There it proves that passive-output programs with at most two input accesses compute only degree-one polynomials, and that with two registers
\[
D^{\mathrm{pass}}_{2,K}(t)=t-1.
\]
The paper also gives four-access high-degree constructions in characteristic zero and in sufficiently large positive characteristic.

The theorem above identifies the sharp obstruction to extending the two-access lower bound to positive characteristic. The failure is exactly the Frobenius/additive-polynomial phenomenon. In the two-register proof of the characteristic-zero frontier, mixed terms from expansions of \(H(\tau+ax)\) force a Vandermonde system. For
\[
H(Z)=Z^{p^e},
\]
all mixed terms disappear:
\[
(\tau+ax)^{p^e}=\tau^{p^e}+a^{p^e}x^{p^e}.
\]
Thus the characteristic assumption is structurally essential, not only an artifact of the exponential-operator proof.

The earlier MFCS 2025 register-program paper develops positive-characteristic constructions over finite fields, including four-access programs for arbitrary univariate polynomials, but the targeted searches described in `REVIEW.md` found no two-access Frobenius construction or the exact two-register classification above.

## Verification

The proof is symbolic and does not depend on finite computation. The companion script `artifacts/verify_two_call_additive.py` checks the formal binomial criterion for small prime characteristics and verifies that the mixed coefficients in
\[
A(T+X)-A(T)-A(X)
\]
vanish exactly for the tested Frobenius powers. Its recorded output is in `artifacts/verification.txt`.

## Limitations

- The exact classification is for the two-register passive-output model and at most two input accesses. The unbounded-degree corollary for more registers follows only because the same two-register construction remains available; it is not a classification of all two-access programs with many work registers.
- The result concerns univariate commutative-field register programs. It does not imply analogous Frobenius simplifications for noncommutative matrix rings.
- Over finite fields, polynomial functions have non-unique polynomial representatives. The formal identities proved here remain valid, but any degree parameter for functions must specify a canonical representative or another convention.
- No claim is made that additive-polynomial folklore itself is new. The claimed contribution is its exact interaction with two-call passive register programs and the resulting characteristic-\(p\) collapse of the recent degree/access frontier.
- Because the construction is very short once Frobenius is considered, folklore and near-simultaneous priority risk are material.

## References

1. Antoine Vinciguerra, *An Operator Approach to Register Programs for Catalytic Computing*, arXiv:2609.18692, 2026. https://arxiv.org/abs/2609.18692
2. Yaroslav Alekseev, Yuval Filmus, Ian Mertz, Alexander Smal, Antoine Vinciguerra, *Catalytic Computing and Register Programs Beyond Log-Depth*, MFCS 2025, LIPIcs 345, Article 6. https://doi.org/10.4230/LIPIcs.MFCS.2025.6
3. R. W. K. Odoni, *On the Galois groups of iterated generic additive polynomials*, Mathematical Proceedings of the Cambridge Philosophical Society 121(1), 1997, 1-6. https://doi.org/10.1017/S0305004196001168
