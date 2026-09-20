# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The main theorem reduces to two standard exact facts about Fibonacci divisibility:

1. \(q\mid F_n\) if and only if \(z(q)\mid n\);
2. for an odd prime \(q\neq5\), if \(z(q)\mid n\), then
   \[
   v_q(F_n)=v_q(F_{z(q)})+v_q(n/z(q)).
   \]

The recent source itself records \(z(q)\mid\pi(q)\) and \(\pi(q)\mid q^2-1\) for \(q\neq5\). Hence \(q\nmid\pi(q)\). Once \(z(q)\mid r\), the affine progression
\[
r/z(q)+t\,\pi(q)/z(q)
\]
has invertible slope modulo every power of \(q\). Exactly one residue class of \(t\) modulo \(q^s\) therefore has \(q\)-adic valuation at least \(s\), giving density \(q^{-s}\). This proves the full \(q^a\)-density formula.

The totient consequence is also exact: if \(q\mid\varphi(F_m)\) and \(q^2\nmid F_m\), then in the prime factorization of \(F_m\) some prime \(p\neq q\) must satisfy \(q\mid p-1\).

The result does not infer nonexistence of Wall--Sun--Sun primes from computation. It treats the Wall--Sun--Sun branch explicitly. The theorem is stated for \(q
eq5\) to match the source lemma under correction; no necessity claim about that exclusion is made for the density formula itself.

## Source audit

The current version inspected was arXiv:2604.17847v3, last revised 22 April 2026. Its summary labels Theorem 4.2 as partial: deterministic for \(k\le31\), computational evidence for \(32\le k\le100\), with the universal statement conjectural.

More importantly for the present result, Lemma 4.3 claims that for every odd \(q\neq5\) with \(S(q)\neq\varnothing\), external primes \(p\equiv1\pmod q\) occur infinitely often along a class in \(S(q)\). In its proof, after reducing the alternative witness to \(q^2\mid F_m\), it states that \(q\) is not a Wall--Sun--Sun prime because no such primes are known in a stated computational range, and therefore substitutes \(z(q^2)=qz(q)\). That is not a valid universal deduction: the existence of Wall--Sun--Sun primes remains open.

The new density theorem shows precisely what changes in the omitted branch. For non-Wall--Sun--Sun \(q\), the prime-power witness has density at most \(1/q\), which validates and strengthens the intended external-witness conclusion. For hypothetical Wall--Sun--Sun \(q\), every class divisible by \(z(q)\) has \(q^2\mid F_m\) identically, so the displayed proof cannot exclude the prime-power mechanism.

No assertion is made that Lemma 4.3's conclusion itself is false in the Wall--Sun--Sun case.

## Originality

**PASS, to the best of our knowledge.**

The exact lifting law and Wall--Sun--Sun characterization are classical and are not claimed as new. Searches were directed at the combination that matters here: \(S(q)\), Euler totients of Fibonacci numbers, Wall--Sun--Sun/Fibonacci--Wieferich primes, ranks of apparition, square divisibility along Pisano-period residue classes, and density of prime-power witnesses.

The current primary source arXiv:2604.17847v3 was read through the relevant theorem, Lemma 4.3, Conjecture 4.4, and stated open problems. It does not give the \(q^a\)-density formula and its Lemma 4.3 proof omits the hypothetical Wall--Sun--Sun case.

Classical references of Wall, Vinson, Sanna, and McIntosh--Roettger supply the divisibility and lifting ingredients but do not, in the material identified, formulate the Fibonacci-totient residue-class consequence. Bragman--Rowland (2025) studies a different notion of density: the proportion of residue values attained modulo increasing powers of a prime.

No inaccessible paper was identified whose metadata or available description specifically suggests this \(S(q)\) density theorem. The main residual risk is unindexed contemporaneous commentary or a correction to the April 2026 preprint.

## Value

**PASS.**

The result does three useful things at once:

- gives an exact closed formula for every prime-power witness density \(q^a\mid F_m\) inside a Pisano-period residue class;
- converts the intended non-Wall--Sun--Sun conclusion of Lemma 4.3 from mere infinitude to an explicit density lower bound \(1\) or \(1-1/q\) for external witnesses;
- isolates the hypothetical Wall--Sun--Sun branch, where prime-square divisibility becomes an automatic mechanism making \(S(q)\) nonempty on all multiples of \(z(q)\).

This is structurally relevant because the omitted branch is tied to a major unresolved exceptional-prime phenomenon, not to a finite computational edge case.

## Limitations

No Wall--Sun--Sun prime is exhibited or asserted to exist. The result does not settle Conjecture 4.4, the Sophie Germain uniqueness conjecture, or the existence of external witnesses in the Wall--Sun--Sun branch. It corrects the logical scope of the prime-square exclusion and determines that mechanism exactly.
