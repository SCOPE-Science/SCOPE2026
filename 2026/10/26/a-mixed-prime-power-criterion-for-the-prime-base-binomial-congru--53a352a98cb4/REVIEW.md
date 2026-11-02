# Independent mathematical audit

## correctness

PASS

Write n=q^t p^e. Legendre digit-sum formula gives v_q(binomial(qn,n))=s_q((q−1)p^e)/(q−1), and q^n is zero mod q^t, proving the third criterion exactly. Davis–Webb/Meštrović prime-power congruence for p≥5 reduces binomial(q^{t+1}p^e,q^t p^e) modulo p^e to B_{t,r} at r=floor((e−1)/3). Lucas congruence gives B mod p=C_t mod p. As q is a p-adic unit, q^{q^t p^e} is congruent mod p^e to Teichmuller(q)^{q^t}; unique (p−1)-st roots of unity are characterized by their mod-p residue and B^(p−1)=1 mod p^e. Conditions (1) and (2) thus give the p-part. CRT combines coprime prime-power moduli. Correct boundary e=1,2,3 has r=0; at e=4 n=3*5^4 comparison binom(45,15) mod625=584 vs binom(9,3) mod625=84 shows lift necessary for reduction. Fresh independent exact arithmetic compared direct and predicted criteria for 44 prime tuples and the fourth-layer witness.

## originality

PASS

Guedes–Machado (2026), Theorem 3.1, already gives exact two-part criterion for n=q^t p with a single p factor; the e=1 special case is unequivocally prior. Meštrović (2012) proves the Davis–Webb compression for arbitrary binomial coefficients, not a complete mixed q^t p^e prime-base congruence classification; a published Resultary result on prime-power towers concerns n=p^e without the distinct q^t factor. The assessed statement combines these ingredients with the higher p-adic Teichmuller lift and digit sum for all e and provides new e=2,3 examples. It is a potentially straightforward consequence of classical p-adic tools, a material priority/value risk retained explicitly; no inspected stronger single theorem was found that states or directly specializes to the full mixed classification.

## value

PASS

The congruence is an explicitly studied natural composite-modulus arithmetic problem, and this gives a complete finite decision criterion for every mixed exponent e≥1, including the sharp first-three-layer fixed-binomial reduction and genuine nontrivial squared/cubed examples n=1127,775,3875. Although it assembles classical lemmas, the exact all-exponent mixed-prime obstruction is a useful self-contained invariant/criterion rather than an arbitrary finite table or mere parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
