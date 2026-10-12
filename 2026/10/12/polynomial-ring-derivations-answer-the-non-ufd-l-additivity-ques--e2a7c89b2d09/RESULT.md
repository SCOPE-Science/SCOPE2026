# Polynomial-ring derivations answer the non-UFD L-additivity question

## Finding
Let \(A\) be any Noetherian integral domain that is not a unique factorization domain. Then
\[
J=A[X]
\]
is a factorization domain that is not a UFD, and the formal derivative
\[
D_X:J\longrightarrow J
\]
is a nonzero L-additive function.

Here L-additive has the definition used by Murashka--Goncharenko--Goncharenko: with the completely multiplicative companion
\[
h(F)=F,
\]
one requires
\[
D_X(FG)=D_X(F)h(G)+D_X(G)h(F).
\]
Thus Question 26 in their paper has an affirmative answer. A concrete example is
\[
J=\mathbb Z[\sqrt{-5}][X].
\]

## Assumptions and scope
A factorization domain means an integral domain in which every nonzero nonunit factors into irreducibles. No uniqueness of irreducible factorization is assumed.

The theorem uses only that \(A\) is a Noetherian integral domain and is not a UFD. The polynomial variable \(X\) is an indeterminate over \(A\). Formal differentiation is coefficientwise:
\[
D_X\left(\sum_{k=0}^{n}a_kX^k\right)
=
\sum_{k=1}^{n}k a_kX^{k-1}.
\]

The claim concerns nonzero L-additive functions in the sense of Question 26. It does not claim that \(D_X\) is the factorization-normalized arithmetic derivative that assigns the value \(1\) to a chosen representative of every irreducible class.

## Proof
Because \(A\) is Noetherian, Hilbert's basis theorem implies that \(A[X]\) is Noetherian. Every Noetherian integral domain satisfies the ascending chain condition on principal ideals, and every domain with that condition is atomic. Hence \(J=A[X]\) is a factorization domain.

Next, \(J\) cannot be a UFD. Since \(A\) is not a UFD and is already Noetherian, it is atomic but has some element with two inequivalent irreducible factorizations in \(A\). Every irreducible constant \(a\in A\) remains irreducible in \(A[X]\): if
\[
a=F(X)G(X),
\]
then the degree formula in the integral domain \(A[X]\) gives
\[
0=\deg a=\deg F+\deg G,
\]
so both factors are constants. Also the units of \(A[X]\) are exactly the units of \(A\). Therefore the two inequivalent factorizations from \(A\) remain inequivalent in \(A[X]\), and \(J\) is not a UFD.

Finally, the identity map
\[
h:J\longrightarrow J,\qquad h(F)=F,
\]
is completely multiplicative. Formal differentiation satisfies the polynomial product rule
\[
D_X(FG)=D_X(F)G+F D_X(G)
       =D_X(F)h(G)+D_X(G)h(F)
\]
for all \(F,G\in J\). Hence \(D_X\) is L-additive with respect to \(h\). It is nonzero because
\[
D_X(X)=1.
\]
This proves the general theorem.

For a fully explicit example, take
\[
A=\mathbb Z[\sqrt{-5}].
\]
It is Noetherian because it is finitely generated as a \(\mathbb Z\)-module. It is not a UFD, as witnessed by
\[
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
\]
With the norm
\[
N(a+b\sqrt{-5})=a^2+5b^2,
\]
there are no elements of norm \(2\) or \(3\). Consequently \(2\), \(3\), and \(1\pm\sqrt{-5}\) are irreducible: a nontrivial factorization of \(2\) would require a factor of norm \(2\), one of \(3\) would require norm \(3\), and one of \(1\pm\sqrt{-5}\), whose norm is \(6\), would require a factor of norm \(2\) or \(3\). The only units have norm \(1\), hence are \(\pm1\), and the displayed irreducibles are pairwise nonassociate across the two factorizations. Thus
\[
\mathbb Z[\sqrt{-5}][X]
\]
is an explicit non-UFD factorization domain carrying the nonzero L-additive function \(D_X\).

## Verification
The accompanying `verify.py` performs two finite regression checks on the explicit example.

First, it verifies the two factorizations of \(6\), the norm values used in the irreducibility proof, the absence of norm-\(2\) and norm-\(3\) elements by the exact size reduction in the proof, and the unit calculation for norm \(1\).

Second, it represents coefficients in \(\mathbb Z[\sqrt{-5}]\), enumerates a finite family of low-degree polynomials, and checks the formal product rule exactly. These computations are regression evidence only. Atomicity of Noetherian domains, Hilbert's basis theorem, persistence of nonunique constant factorizations, and the product rule for arbitrary polynomials are proved symbolically above and are not inferred from finite tests.

## Relationship to prior work
Murashka--Goncharenko--Goncharenko define L-additivity over rings and explicitly ask in Question 26 whether any factorization domain that is not a UFD admits a nonzero L-additive function. Their definition says that the case \(h(x)=x\) is called L-additive.

Haukkanen--Mattila--Merikoski--Tossavainen study a more restrictive factorization-normalized arithmetic derivative on non-UFDs. Their construction requires chosen irreducibles to have derivative \(1\), and they prove failure for broad classes of quadratic-integer non-UFDs. That negative result does not rule out the present formal derivative because \(D_X\) is only required to satisfy the L-additive Leibniz identity and does not send every irreducible to \(1\).

Emmons--Xiao likewise explain that the factorization-normalized UFD construction fails in non-UFDs and develop a different extension to number fields. Their obstruction is therefore compatible with this theorem.

Targeted searches for Question 26, nonzero L-additive functions on non-UFD factorization domains, polynomial-ring formal derivatives, and the explicit ring \(\mathbb Z[\sqrt{-5}][X]\) did not locate this construction or a statement implying it.

## Limitations
The theorem gives a broad existence class but does not classify all non-UFD factorization domains admitting nonzero L-additive functions.

It also does not solve the distinct problem of constructing the classical factorization-normalized arithmetic derivative on a non-UFD. The construction exploits the independent polynomial variable \(X\); it makes no claim that a comparable nonzero derivation exists on every non-UFD factorization domain itself.

The main residual originality risk is that this elementary polynomial-ring observation may occur in an unindexed algebra note or informal discussion not surfaced by the targeted searches.

## References
1. Viachaslau I. Murashka, Andrey D. Goncharenko, and Irina N. Goncharenko, “Leibniz-Additive Functions on UFD's,” Journal of Integer Sequences 23 (2020), Article 20.10.3.
2. Pentti Haukkanen, Mika Mattila, Jorma K. Merikoski, and Timo Tossavainen, “Can the Arithmetic Derivative be Defined on a Non-Unique Factorization Domain?”, Journal of Integer Sequences 16 (2013), Article 13.1.2.
3. Caleb Emmons and Xiao Xiao, “A Generalization of Arithmetic Derivative to p-adic Fields and Number Fields,” Notes on Number Theory and Discrete Mathematics 30 (2024), 357--382.
