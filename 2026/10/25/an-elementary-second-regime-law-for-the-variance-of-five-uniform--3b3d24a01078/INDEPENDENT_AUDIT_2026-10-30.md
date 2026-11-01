# Independent mathematical audit

## correctness

PASS

For five iid U[0,1] variables with sample variance divisor four, orthogonal mean/contrast coordinates give F(y)=sqrt(5) integral_{||v||<=sqrt(4y)}(1-R(v))_+ dv over H={sum v_i=0}. Splitting (1-R)_+=1-R+(R-1)_+ recovers the known low branch plus correction. Two distinct positive ordered coordinate-difference violations v_i-v_j>1 require ||v||^2>=2/(2+q)>=2/3, where q<=1 is their Gram product; hence for 1/8<=y<=1/6 the 20 caps have disjoint interiors. Integrating the three-ball cross-sections yields the stated arccos/sqrt formula. The cap integral has exact onset 4096*pi*sqrt(10)/21*(y-1/8)^(7/2)+O((y-1/8)^(9/2)). Independent mpmath quadrature agrees at 1/8, .13, .14, and 1/6 (F_5(1/6)=0.96674377169081645); normalized onset ratio tends to one. Continuum proof is geometry and integration, not finite sampling.

## originality

PASS

Comparison is by exact mathematical statements, quantifiers and implications, with strong prior premises acknowledged; best-of-knowledge historical priority subject to the explicit unread-paper and alias risks.

## value

PASS

A complete exact, elementary second interval for the natural five-sample uniform unbiased-variance CDF fills a genuine boundary immediately past the known low branch and quantifies a nonanalytic 7/2 onset. It is a motivated adjacent regime, not a single evaluated probability or a claim to full-support closure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
