# Exact component and fibre-rank law for the three-block period-doubling lift

## Finding
Let \(\kappa\geq2\) be an integer, let \(\Gamma\) be the binary substitution \(1\mapsto10\), \(0\mapsto11\), and let \(Y_{\mathrm{pd}}\subset\{0,1\}^{\mathbb Z}\) be its two-sided minimal subshift. For \(x\in(\mathbb Z/\kappa\mathbb Z)^{\mathbb Z}\), define \(\eta_{\kappa,3}(x)_j=x_{j+2}-x_j\pmod\kappa\). Set \(X_\kappa=\eta_{\kappa,3}^{-1}(Y_{\mathrm{pd}})\) and \(q(\kappa)=2^{\nu_2(\kappa)}\), with \(q(\kappa)=1\) for odd \(\kappa\).

**Theorem.** The shift on \(X_\kappa\) has exactly \(q(\kappa)\) disjoint minimal components. Every component \(M\) meets every fibre \(\eta_{\kappa,3}^{-1}(y)\), for every \(y\in Y_{\mathrm{pd}}\), in exactly \(\kappa^2/q(\kappa)\) points. Thus all components have the same fibre rank. In particular, odd moduli give one minimal lift, while \(\kappa=2^r m\), \(m\) odd, gives exactly \(2^r\) components of common rank \(2^r m^2\).

## Assumptions and scope
The base is precisely the two-sided period-doubling subshift of the displayed substitution; the lift uses the **three-symbol difference code** and not an arbitrary permutative block code. The integer \(\kappa\) is at least two. A minimal component means a nonempty closed invariant subset on which the shift acts minimally. Fibre rank means the cardinality of its intersection with each inverse-image fibre. No measure-theoretic classification of arbitrary invariant measures is claimed.

## Proof
**1. Two substitution phases and the lifted cocycle.** The substitution sends a binary sequence \(z\) to the interleaving \(\Gamma(z)_{2j}=1\), \(\Gamma(z)_{2j+1}=1-z_j\). Its primitive subshift has no occurrence of \(00\). Every sequence in \(Y_{\mathrm{pd}}\) lies in \(Y_0=\Gamma(Y_{\mathrm{pd}})\) or \(\sigma Y_0\), by approximating with shifts of long substitution words and selecting the parity of each shift. These closed sets are disjoint: an element in both would have all symbols equal to one, which is excluded by the language. The shift exchanges these two clopen phases and its square preserves each. The map \(z\mapsto\Gamma(z)\) conjugates \(\sigma\) on the original base to \(\sigma^2\) on \(Y_0\).

A point of the three-block lift is uniquely specified by its base image \(y\) and the initial pair \((a,b)=(x_0,x_1)\in G=(\mathbb Z/\kappa\mathbb Z)^2\): the recurrence \(x_{j+2}=x_j+y_j\) determines every coordinate in both directions. Over \(Y_0\), two steps of the lifted shift are therefore conjugate to
\[
S(z,a,b)=(\sigma z,a+1,b+1-z_0)\pmod\kappa.
\]
Its cocycle is \(c(z)=(1,1-z_0)\in G\). Each minimal component of the full one-step lift meets the phase over \(Y_0\) in one minimal \(S\)-component, and conversely every minimal \(S\)-component generates exactly one minimal one-step component by adjoining its image under one shift. Thus the two systems have the same number of components, and the same fibre rank over their respective base points.

**2. Exact return words on nested cylinders.** Put \(\tau_n=\Gamma^n(1)\), of length \(2^n\), and let \(u_n\) denote \(\tau_n\) with its last symbol removed. The cylinders \(U_n=\{z:z_{[0,2^n-2]}=u_n\}\), \(n\geq2\), are nonempty and nested, and their defining lengths tend to infinity. Consecutive occurrences of \(u_n\) in the fixed right-infinite period-doubling sequence are separated by exactly two possible return words, \(\tau_{n-1}\) and \(\tau_n\). Here a return word includes the first occurrence's starting position and ends just before the next starting position, so overlaps of long cylinders are allowed.

For completeness, the base case \(n=2\) has \(u_2=101\). An occurrence at an odd index in a substitution-aligned word would force consecutive zeroes in the preimage, impossible in the period-doubling language. At an even index, \(101\) occurs exactly when the corresponding preimage symbol is \(1\). Consecutive \(1\)'s in the fixed sequence have return words \(1\) and \(10\), hence their images under \(\Gamma\) are \(\tau_1=10\) and \(\tau_2=1011\). For \(n\geq2\), the same parity obstruction holds because \(u_{n+1}\) begins in \(101\). At even indices, an occurrence of \(u_{n+1}\) is equivalent to an occurrence of \(u_n\) in the substituted preimage: \(\Gamma(u_n)\) supplies the first \(2^{n+1}-2\) symbols and the next output symbol is always \(1\). Substitution therefore sends both return words for \(u_n\) to the two return words for \(u_{n+1}\). Both types recur by primitivity. The same return-word set holds in every element of the two-sided minimal subshift by equality of finite languages.

The number \(s_n\) of symbols equal to one in \(\tau_n\) is
\[
s_n=\frac{2^{n+1}+(-1)^n}{3}.
\]
Indeed, \(s_0=s_1=1\), and \(s_{n+1}=2^{n+1}-s_n\) follows by counting substituted ones. Both return words therefore carry cocycle increments
\[
v_n=(2^{n-1},2^{n-1}-s_{n-1}),\qquad
w_n=(2^n,2^n-s_n)
\]
with coordinates reduced modulo \(\kappa\). Their integral determinant is
\[
\det(v_n,w_n)=2^{n-1}(2s_{n-1}-s_n)=(-1)^{n+1}2^{n-1}.
\]
Since \(s_{n-1}\) is odd, the entries of the two-by-two integer matrix \([v_n\ w_n]\) have greatest common divisor one. Its Smith normal form is consequently \(\operatorname{diag}(1,2^{n-1})\). The subgroup \(H_n=\langle v_n,w_n\rangle\leq G\) has exact index
\[
[G:H_n]=\gcd(\kappa,2^{n-1}).
\]
These subgroups are nested decreasing because \(U_{n+1}\subset U_n\), and eventually stabilize at index \(q(\kappa)\).

**3. Why return subgroups are exactly minimal-component stabilizers.** We record the finite-group-extension argument to avoid assuming that return permutations merely bound the number of components. For the skew product \(S\), every point is almost periodic: this follows from the standard almost-periodicity theorem for finite permutative lifts of minimal subshifts (Kang--Jäger, Theorem 4.1, quoting Hedlund), applied to the original lift, and also to its clopen square-shift phase. Consequently this phase is a finite disjoint union of minimal components. They are clopen. Since translations \(T_g(z,h)=(z,h+g)\), \(g\in G\), commute with \(S\), the translations act transitively on the components: each projects onto the entire minimal base, and a translate can match a prescribed point in any fixed base fibre.

Fix a two-sided \(z_*\in Y_{\mathrm{pd}}\) whose nonnegative coordinates form the substitution fixed point, and let \(M\) contain \((z_*,0)\). Define its subgroup stabilizer
\[
H=\{g\in G:T_g(M)=M\}.
\]
Every component is a translate of \(M\); each intersection with a fibre is a coset of \(H\). Thus the number of components is \([G:H]\) and their common fibre rank is \(|H|\).

We show \(H=H_n\) for all sufficiently large \(n\). First, component labels for points with the same fibre coordinate depend only on the *future* base coordinates: if \(z\) and \(z'\) agree at all nonnegative positions, their cocycle sums agree at every positive time, while \(d(\sigma^t z,\sigma^t z')\to0\) as \(t\to\infty\). Points in two distinct clopen invariant components have a strictly positive separation, a contradiction. Because the finite-valued component-label map is continuous on the compact skew space and is determined by the future, there is a common finite prefix length after which its value is constant for each fixed \(g\) on cylinders with that prefix. Since the cylinders \(U_n\) shrink around the right-infinite fixed word, choose \(n\) large enough that every point \((z,g)\), \(z\in U_n\), has the same label as \((z_*,g)\). For a return from \(U_n\) to itself the cocycle increment must therefore stabilize \(M\); in particular \(v_n,w_n\in H\), giving \(H_n\subseteq H\).

Conversely, if \(h\in H\), the point \((z_*,h)\) belongs to the same minimal component as \((z_*,0)\). Its arbitrarily small cylinder neighborhood \(U_n\times\{h\}\) must meet the positive orbit of \((z_*,0)\). Any such return is a concatenation of consecutive \(U_n\)-return words, so its cocycle increment \(h\) belongs to \(H_n\). Hence \(H\subseteq H_n\) for every \(n\). For large \(n\), equality follows, and the Smith calculation yields \([G:H]=q(\kappa)\) and \(|H|=\kappa^2/q(\kappa)\). Finally, conjugating back to the one-step lift preserves those numbers. This completes the proof.

## Verification
The proof is infinite and rests on the parity-recognizable substitution, the exact return-word induction, the Smith form, and the component-stabilizer equality. The standalone script `check_components.py` checks return-gap lengths for \(n=2,\ldots,9\), the determinant formula, and subgroup indices for moduli \(2\leq\kappa\leq17\). It is an independent finite sanity check, not an exhaustive proof. Run with `python3 check_components.py` from a directory containing that file; it uses only the Python standard library.

## Relationship to prior work
Kang and Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1 (2026), Theorem 1.7 and Proposition 4.10, determine **whether** the period-doubling three-block lift is minimal: precisely when \(\kappa\) is odd. Their Theorem 4.1 and Corollary 4.2 establish decomposition into finitely many minimal pieces, and Lemma 4.11 establishes constancy of fibre rank inside an individual piece. None of these gives the exact component count and common rank for all \(\kappa\). The result here computes both numbers, including every even modulus. Prior period-doubling return-word literature supplies combinatorial background, not the arithmetic-index conclusion.

## Limitations
No claim is made for odd block lengths at least five, general substitution systems, or nonabelian cocycles. The result concerns component counts and fibre ranks, not spectrum or invariant-measure simplex. Return-word and Smith computations alone do not imply the dynamical classification without the separate stabilizer argument. Overlap with an equivalent unindexed older description of a finite odometer extension cannot be categorically excluded; independent mathematical review has not occurred.

## References
1. Zeyu Kang and Tobias Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1, first posted 2026-09-01, https://arxiv.org/html/2609.01140v1 .
2. G. A. Hedlund, *Endomorphisms and automorphisms of the shift dynamical system*, Mathematical Systems Theory 3 (1969), 320–375; Theorem 12.4, as cited and used in Kang--Jäger, Theorem 4.1.
3. Yu-Ke Huang and Zhi-Ying Wen, *Envelope Words and the Reflexivity of the Return Word Sequences in the Period-doubling Sequence*, arXiv:1703.07157 (2017), background on period-doubling return words.
