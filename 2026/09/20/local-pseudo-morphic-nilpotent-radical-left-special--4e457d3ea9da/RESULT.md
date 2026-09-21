# Local left pseudo-morphic rings with nilpotent radical are left special

Let \(R\) be a ring with identity, let \(J=J(R)\), and write
\[
\ell(x)=\{r\in R:rx=0\}.
\]
An element \(a\in R\) is **left pseudo-morphic** when \(Ra=\ell(b)\) for some
\(b\in R\). A ring is left pseudo-morphic when every element is left
pseudo-morphic.

Camillo and Nicholson asked whether every local left pseudo-morphic ring with
nilpotent Jacobson radical is left special, equivalently whether its radical must
be a principal left ideal. The answer is affirmative. In fact, it is enough to
assume the pseudo-morphic condition for a single nonzero element in the last
nonzero radical power.

## Theorem

Let \(R\) be local and suppose \(J\) is nilpotent and nonzero. Let \(n\ge 2\) be
minimal with \(J^n=0\). If there is a nonzero \(a\in J^{n-1}\) such that
\[
Ra=\ell(c)
\]
for some \(c\in R\), then
\[
\boxed{J=Rc.}
\]
Consequently \(c\) is nilpotent and \(R\) is left special.

In particular, every local left pseudo-morphic ring with nilpotent Jacobson
radical is left special. This gives an affirmative answer to Question 1 of
Camillo--Nicholson (2015).

## Proof

Put \(S=J^{n-1}\). Because \(a\ne0\) and \(J^n=0\),
\[
J\subseteq \ell(a).
\]
Conversely, if \(r\notin J\), then \(r\) is a unit because \(R\) is local, so
\(ra=0\) would force \(a=0\). Hence
\[
\ell(a)=J.
\]
Right multiplication by \(a\) therefore gives an isomorphism of left
\(R\)-modules
\[
R/J\cong Ra.
\]
Thus \(Ra\) is simple. Since \(a\in S\), we also have \(Ra\subseteq S\).

By hypothesis, \(Ra=\ell(c)\). This annihilator is nonzero and proper, so \(c\)
is neither zero nor a unit. Hence \(c\in J\). Since \(S=J^{n-1}\),
\[
Sc\subseteq J^n=0,
\]
so \(S\subseteq \ell(c)=Ra\). Combined with \(Ra\subseteq S\), this yields
\[
S=Ra=\ell(c).
\]
In particular, \(S\) is simple.

Consider right multiplication by \(c\),
\[
\rho_c:{}_RR\longrightarrow {}_RRc,\qquad r\longmapsto rc.
\]
Its kernel is \(\ell(c)=S\), hence
\[
R/S\cong Rc. \tag{1}
\]
For each \(1\le i\le n-1\), restricting \(\rho_c\) to \(J^i\) gives
\[
J^i/S\cong J^ic\subseteq J^{i+1}, \tag{2}
\]
because \(S\subseteq J^i\) and \(c\in J\).

Equation (2) shows by downward induction that every \(J^i\) has finite left
composition length: \(J^{n-1}=S\) is simple, and finite length of \(J^{i+1}\)
implies finite length of its submodule \(J^ic\), hence of \(J^i/S\), and then of
\(J^i\). Thus \(J\) has finite length. Since \(R/J\) is simple, \(R\) also has
finite left composition length.

Now (1) and simplicity of \(S\) give
\[
\operatorname{length}(Rc)=\operatorname{length}(R)-1.
\]
Likewise, since \(R/J\) is simple,
\[
\operatorname{length}(J)=\operatorname{length}(R)-1.
\]
But \(c\in J\), so \(Rc\subseteq J\). Equality of their finite lengths forces
\[
Rc=J.
\]
Finally \(c\in J\) and \(J^n=0\) imply \(c^n=0\). A local ring with
\(J=Rc\) for a nilpotent \(c\) is left special. This proves the theorem. \(\square\)

If \(J=0\), then \(R\) is a division ring and is left special as well (take
\(c=0\)). Hence the stated corollary covers all nilpotent radicals.

## Context and significance

Camillo and Nicholson introduced the question in their study of rings whose left
principal ideals are left principal annihilators. They record the standard
equivalent descriptions of a left special ring, including: \({}_RR\) is uniserial
of finite length; and \(R\) is local with \(J=Rc\) for a nilpotent \(c\). Their
Question 1 asks precisely whether local + left pseudo-morphic + nilpotent \(J\)
already forces this situation.

The proof above uses only one pseudo-morphic witness \(a\) from the last nonzero
radical layer. The mechanism is that \(Ra\) becomes the simple last radical layer,
while its annihilator representation \(Ra=\ell(c)\) makes multiplication by \(c\)
embed each successive quotient \(J^i/J^{n-1}\) into \(J^{i+1}\). Nilpotence then
forces finite length, after which the isomorphism \(R/J^{n-1}\cong Rc\) forces
\(Rc=J\).

## Originality and limitations

The conclusion is asserted to the best of our knowledge. Targeted searches for the
2015 question, left pseudo-morphic local rings with nilpotent radical, the equivalent
CEFR terminology, and principal-annihilator formulations did not locate a published
resolution. Later work on comorphic rings and on the stronger property (P) gives
chain-type conclusions under stronger hypotheses and therefore does not imply the
theorem above.

A 2023 paper of Neishabouri--Tolooei--Bagheri proves that left pseudo-morphic rings
are exactly rings whose left regular module is co-epi-finite-retractable (CEFR) and
announces further properties of such rings. Its full text was not inspected here;
this is the most relevant unresolved literature risk because an equivalent result
could be stated there in CEFR language. The accessible abstract does not state the
local nilpotent-radical conclusion. The 2015 corrigendum to Camillo--Nicholson
corrects Lemma 5.6 and Theorem 5.7, not Question 1 or the left-special equivalences
used here.

## References

1. V. Camillo and W. K. Nicholson, *On Rings Where Left Principal Ideals Are Left Principal Annihilators*, International Electronic Journal of Algebra **17** (2015), 199--214. DOI: 10.24330/ieja.266221.
2. V. Camillo and W. K. Nicholson, *Corrigendum to “On Rings Where Left Principal Ideals Are Left Principal Annihilators”*, International Electronic Journal of Algebra **18** (2015), 117--118. DOI: 10.24330/ieja.266208.
3. W. K. Nicholson and E. Sánchez Campos, *Principal Rings with the Dual of the Isomorphism Theorem*, Glasgow Mathematical Journal **46** (2004), 181--191. DOI: 10.1017/S0017089503001654.
4. P. Neishabouri, Y. Tolooei and S. Bagheri, *On modules in which every finitely generated submodule is a kernel of an endomorphism*, Communications in Algebra **51** (2023), 841--858. DOI: 10.1080/00927872.2022.2115504.
5. M. Alkan, W. K. Nicholson and A. Ç. Özcan, *Comorphic rings*, Journal of Algebra and Its Applications **17** (2018), 1850075. DOI: 10.1142/S0219498818500755.
6. T. C. Quynh, M. T. Koşan and J. Žemlička, *A new member of Nicholson's morphic folks*, Journal of Algebra **664** (2025), 268--287. DOI: 10.1016/j.jalgebra.2024.10.009.
