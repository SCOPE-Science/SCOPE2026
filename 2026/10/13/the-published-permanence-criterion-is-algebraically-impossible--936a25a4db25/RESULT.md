# The published permanence criterion is algebraically impossible

## Finding

The source's \(n\)-prey, one-predator model assumes
\[
0<c_i<p_i.
\]
Its permanence theorem requires, with
\[
M=n+\sum_i a_i,
\]
that
\[
\frac{p_i}{a_i}<\frac1M.
\]
The proof also defines
\[
M_i=1-\frac{p_i}{a_i}M,
\qquad
R_i=\min\left\{\frac{M_i}{2},H_i\right\}.
\]
Therefore
\[
R_i\le\frac{M_i}{2}.
\]

These statements imply the universal bound
\[
\sum_i c_iR_i<\frac18.
\]
The same theorem instead requires
\[
\sum_i c_iR_i>1+\sum_i b_i>1.
\]
Hence its sufficient conditions cannot be satisfied simultaneously.

## Assumptions and scope

All model parameters are positive and satisfy the source's conversion-versus-predation restriction
\[
c_i<p_i.
\]
The argument uses conditions (5) and (6) and the quantities \(M_i\) and \(R_i\) exactly as printed.

The conclusion is that the sufficient permanence theorem has an empty hypothesis set. It does not prove that the model has no permanent solutions and does not derive a replacement permanence criterion.

## Proof

Set
\[
M=n+\sum_i a_i,
\qquad
q_i=\frac{p_iM}{a_i}.
\]
Condition (5) gives
\[
0<q_i<1.
\]
Because
\[
M_i=1-q_i
\]
and
\[
R_i\le\frac{M_i}{2},
\]
the model assumption \(c_i<p_i\) gives
\[
c_iR_i
<
p_i\frac{1-q_i}{2}.
\]
Using
\[
p_i=\frac{a_iq_i}{M},
\]
\[
c_iR_i
<
\frac{a_i}{2M}q_i(1-q_i).
\]
Since
\[
q_i(1-q_i)\le\frac14,
\]
\[
c_iR_i<\frac{a_i}{8M}.
\]
Summation yields
\[
\sum_i c_iR_i
<
\frac{\sum_i a_i}{8M}
<
\frac18,
\]
because \(M=n+\sum_i a_i>\sum_i a_i\).

Condition (6) requires
\[
\sum_i c_iR_i>1+\sum_i b_i.
\]
As every \(b_i>0\), its right-hand side is strictly larger than \(1\), a contradiction.

The source's final proof step also uses condition (6) to produce a strictly positive lower bound on predator per-capita growth, which would force exponential growth of the predator and conflict with the boundedness established earlier. The algebraic contradiction explains this inconsistency.

## Verification

The bundled `verify.py` verifies
\[
\frac14-q(1-q)=\left(q-\frac12\right)^2
\]
and the substitution
\[
p_i\frac{1-q_i}{2}
=
\frac{a_i}{2M}q_i(1-q_i).
\]
It also performs exact rational sanity checks satisfying condition (5) and \(c_i<p_i\).

The finite checks are not the proof; the universal claim follows from the algebra above.

## Relationship to prior work

The motivating paper presents permanence as a principal qualitative property of its multi-prey Holling-II model and gives Theorem 2 as the sufficient criterion.

Earlier two-prey, one-predator studies establish persistence or permanence in different ecological models under model-specific feasible hypotheses. Those results provide context for the importance of permanence criteria but do not contain the source-specific incompatibility proved here.

Searches by the motivating DOI, exact title, permanence terminology, the quantity involving \(c_iR_i\), and correction terminology did not locate a published repair of Theorem 2.

## Limitations

The result proves vacuity rather than exhibiting a counterexample to a nonempty theorem.

No replacement sharp permanence condition is derived.

A non-indexed author correction could exist outside the checked records.

## References

1. S. Fatah, A. Mustafa, S. Amin, “Predator and n-classes-of-prey model incorporating extended Holling type II functional response for n different prey species,” AIMS Mathematics 8 (2023), 5779–5788. DOI: 10.3934/math.2023291.
2. M. F. Elettreby, “Two-prey one-predator model,” Chaos, Solitons & Fractals 39 (2009), 2018–2027. DOI: 10.1016/j.chaos.2007.06.058.
3. H. Baek, “Species extinction and permanence of an impulsively controlled two-prey one-predator system with seasonal effects,” BioSystems 98 (2009), 7–18. DOI: 10.1016/j.biosystems.2009.06.008.
