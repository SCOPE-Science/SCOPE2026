# Independent mathematical audit

## correctness

PASS

The canonical product partition function gives C/k_B=H_r(y)=f(y/r)+f(y), f(z)=z² exp(-z)/(1+exp(-z))². Differentiating directly gives f'(x)=x/2+O(x³), f''(x)=1/2+O(x²) near zero and f''(y)=exp(-y)(y²-4y+2+O(y² exp(-y))) at infinity. Uniformly on [L,3L], L=log r, both second derivatives entering H_r'' are therefore positive for large r. The first derivative is negative at L and positive at 3L by comparing y/(2r²) with y² exp(-y)(1-2/y+O(exp(-y))). Thus the intermediate root exists, is unique in the window and is a strict local minimum. At the root the comparison gives y=2L+log(2y)+o(1); the window bounds first yield y=2L+O(log L), then y=2L+log L+log 4+o(1). The two heat-capacity terms there are asymptotic to y²/(4r²) and y/(2r²), respectively, giving the height. Bracket the single-gap maximizer at fixed offsets in y for one peak, and in x=y/r for the other: the single-gap derivative dominates in each bracket and has opposite endpoint signs, giving interior maxima. No global critical-point classification is implied. Independent replay: python3 /workspace/branches/reproduction/valley.py solves a stable log-derivative balance at log r=8,20,100,1000; at 1000 the position error is 0.0031436502 and the normalized height is 1.009319554. Finite replay is diagnostic only.

## originality

PASS

The single-gap formula, multiple Schottky features, and asymptotic peak separation under a degeneracy hierarchy are not the contributions assessed. No examined antecedent supplies the separation-window theorem and precise location and height of the valley for the product of two equally weighted nondegenerate independent TLS with a diverging gap ratio. This is a bounded best-of-knowledge conclusion.

## value

PASS

The two individual peak scales do not locate their point of separation. The sharp valley law gives a quantitative benchmark for distinguishing two thermal scales and explains the double logarithm as a balance of algebraic and activation tails. It is useful within the explicitly idealized model without requiring a threshold for every gap ratio or a claim about experimental extraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
