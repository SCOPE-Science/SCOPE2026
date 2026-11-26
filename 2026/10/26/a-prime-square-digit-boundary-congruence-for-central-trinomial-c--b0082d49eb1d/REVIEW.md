# Independent mathematical audit

## correctness

PASS

For Q=1+x+x^(-1) and p>=5, Q(x) divides Q(x^p) integrally in Laurent polynomials by the action of p on primitive cube roots. Its quotient B has exponents strictly between -p and p, and constant term epsilon_p by extracting x^(p-1) from (1-x)/(1-x^3). Reducing Q^p=Q(x^p) modulo p and cancelling Q in the Laurent domain shows Q^(p-1)=B+pA with integral A of support likewise inside (-p,p). Expanding (Q(x^p)+pQA)^m and cancelling one exact Q, the terms containing at least two p factors remain divisible by p^2. The remaining polynomials give (B+mpA)Q(x^p)^(m-1). Only exponent zero of B and A can pair with an exponent divisible by p, yielding the first formula with p CT(A)=T_(p-1)-epsilon_p. The verified Cao–Sun base-index residue and (1+pu)^m=1+mpu modulo p^2 give the second formula for all positive m, including multiples of p, with no division by a trinomial coefficient. Iteration contributes r signs and total exponent p^r-1. An independent direct binomial summation (`python3 /workspace/reproduce.py`) checked 70 pairs including m=p and 2p, and 9 prime-power instances. The finite checks are not the proof.

## originality

PASS

The inspected literature gives the m=1 base case, a general mod-p digit law, higher-power coupled relations, and stronger results on other indices. The supported distinct claim is the explicit mod-p^2 coefficient on the whole pm-1 family. The prime-power statement is credited as its iteration, not as independent novelty. The bounded comparisons do not establish absolute priority.

## value

PASS

This is an exact prime-square lift on a natural full index boundary, well beyond a numerical residue or the published isolated base case. The cyclotomic quotient explains why an entire residue class admits an explicit correction and gives a closed formula for strings of maximal base-p digits without any unit assumption on the smaller trinomial coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
