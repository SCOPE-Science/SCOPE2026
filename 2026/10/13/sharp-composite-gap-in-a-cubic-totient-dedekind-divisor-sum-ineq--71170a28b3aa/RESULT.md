# Sharp composite gap in a cubic totient–Dedekind–divisor-sum inequality
## Finding
For every composite integer \(n\ge4\), let \(\varphi(n)\) denote Euler's totient, let
\[\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right),\]
and let \(\sigma(n)=\sum_{d\mid n}d\). Then
\[\varphi(n)^3+\psi(n)^3+\sigma(n)^3\ge 3n^3+3n^2+9n+291.\]
Equality holds if and only if \(n=4\). Thus, for the cubic inequality of Dimitrov, the exact least additive defect on composite integers is \(290\).

## Assumptions and scope
The variable \(n\) ranges over composite positive integers. No hypothesis is made on the number of prime factors or their exponents. The functions are the classical Euler totient, Dedekind psi, and sum-of-divisors functions. The theorem is an exact sharpening only for the cubic expression; it does not claim an analogous sharp composite constant for other powers.

## Proof
Put
\[x=\psi(n)-n,\qquad y=\sigma(n)-\psi(n).\]
Both are integers. If the distinct prime divisors of \(n\) are \(p_1,\ldots,p_r\), then
\[\frac{\varphi(n)}n=\prod_{i=1}^r\left(1-\frac1{p_i}\right),\qquad
  \frac{\psi(n)}n=\prod_{i=1}^r\left(1+\frac1{p_i}\right).\]
Adding these products cancels the odd-degree elementary symmetric terms, so
\[\varphi(n)+\psi(n)\ge2n.\]
Hence \(\varphi(n)\ge n-x\). Also, on a prime power,
\[\sigma(p^a)=1+p+\cdots+p^a,\qquad \psi(p^a)=p^a+p^{a-1},\]
so multiplicativity gives \(y\ge0\), with \(y=0\) exactly when \(n\) is squarefree.

Define the defect
\[F(n)=\varphi(n)^3+\psi(n)^3+\sigma(n)^3-(3n^3+3n^2+9n+1).\]
Since the cube function is increasing,
\[F(n)\ge G(n,x,y),\]
where
\[G(n,x,y)=(n-x)^3+(n+x)^3+(n+x+y)^3-(3n^3+3n^2+9n+1).\]

First suppose that \(n\) is squarefree and composite. Write \(n=pqm\) with distinct primes \(p<q\) and \(m\ge1\). Since \(\psi(m)\ge m\),
\[x=\psi(n)-n\ge m\bigl((p+1)(q+1)-pq\bigr)=m(p+q+1)\ge6.\]
Here \(y=0\), and direct factorization gives
\[G(n,x,0)=(x-1)\bigl(3n^2+9nx+9n+x^2+x+1\bigr).\]
As \(n\ge6\) and \(x\ge6\), this is at least \(2645\), hence strictly greater than \(290\).

Now suppose that \(n\) is not squarefree. Some \(p^2\mid n\), and therefore
\[x=n\left(\prod_{q\mid n}\left(1+\frac1q\right)-1\right)\ge\frac np\ge2.\]
Also \(y\ge1\), and \(n\ge4\). On the region \(n\ge4\), \(x\ge2\), \(y\ge1\), the partial derivatives of \(G\) are
\[\frac{\partial G}{\partial x}=3\bigl(n^2+6nx+2ny+x^2+2xy+y^2\bigr)>0,\]
\[\frac{\partial G}{\partial y}=3(n+x+y)^2>0,\]
and
\[\frac{\partial G}{\partial n}=3\bigl(2nx+2ny-2n+3x^2+2xy+y^2-3\bigr)>0.\]
Thus
\[F(n)\ge G(n,x,y)\ge G(4,2,1)=290.\]
At \(n=4\), one has \(\varphi(4)=2\), \(\psi(4)=6\), and \(\sigma(4)=7\), so equality is attained. Strict monotonicity in the nonsquarefree region and the squarefree estimate show that no other composite integer can attain it.

## Verification
The symbolic proof above is unbounded. The bundled program `verify.py` separately evaluates \(\varphi\), \(\psi\), and \(\sigma\) from prime factorizations through \(300000\), checks the squarefree/nonsquarefree branch inequalities, and confirms that the composite defect has unique minimum \(290\) at \(n=4\). Its saved output is in `verification_output.txt`.

## Relationship to prior work
Dimitrov's 2024 paper proves, for every \(n\ge2\),
\[\varphi(n)^3+\psi(n)^3+\sigma(n)^3\ge3n^3+3n^2+9n+1.\]
The preprint was first publicly posted as arXiv:2404.19332 on 2024-04-30; the journal version has primary MSC 11A25. The paper proves equality for primes through its base case but does not give a sharp uniform additive improvement restricted to composite integers.

Sándor and Gryszka later proved the all-power refinement
\[\varphi(n)^k+\psi(n)^k+\sigma(n)^k\ge\varphi(n)^k+2\psi(n)^k\ge(n-1)^k+2(n+1)^k\]
for \(k\ge2\). At \(k=3\), its final term is Dimitrov's cubic bound. This stronger parameterized inequality still does not determine the least additional defect on the composite stratum: at \(n=4\), the intermediate estimate leaves only \(163\) units above the cubic baseline, whereas the exact defect is \(290\). The present result uses the discrete gap \(\sigma(n)-\psi(n)\) together with the squarefree/nonsquarefree split to obtain the sharp composite constant.

A 2026 continuation by Dimitrov was also checked. Its displayed main results concern different reciprocal and mixed expressions, followed by conjectures; searches of the accessible full text did not locate this composite cubic constant or the value \(291\). This inspection reduces but does not eliminate the possibility of equivalent statements under unrelated terminology.

## Limitations
The result is a sharp refinement for one cubic expression only. It does not establish sharp composite gaps for the quartic or mixed inequalities in the same literature, nor for arbitrary powers. The computational replay is finite regression evidence and is not used as proof of the infinite statement.

## References
1. S. I. Dimitrov, *Lower bounds on expressions dependent on functions \(\varphi(n)\), \(\psi(n)\) and \(\sigma(n)\), II*, arXiv:2404.19332; DOI 10.7546/nntdm.2024.30.3.547-556.
2. J. Sándor and K. Gryszka, *On certain inequalities for \(\varphi\), \(\psi\), \(\sigma\) and related functions, III*, DOI 10.7546/nntdm.2025.31.2.361-369.
3. S. I. Dimitrov, *Lower bounds on expressions depending on the functions \(\varphi(n)\), \(\psi(n)\) and \(\sigma(n)\), III*, arXiv:2606.12484.
